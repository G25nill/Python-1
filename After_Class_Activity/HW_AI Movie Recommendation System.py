
import os
import random
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from textblob import TextBlob
from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)


# ==========================================
# 1. LOAD THE IMDb DATASET
# ==========================================

# Find the CSV file in the same folder as this Python file
folder = os.path.dirname(os.path.abspath(__file__))
dataset_path = os.path.join(folder, "imdb_top_1000.csv")

try:
    movies = pd.read_csv(dataset_path)

    # Remove unnecessary spaces from column names
    movies.columns = movies.columns.str.strip()

    # Check required columns
    required_columns = [
        "Series_Title", "Genre", "Overview", "IMDB_Rating"
    ]

    for column in required_columns:
        if column not in movies.columns:
            raise ValueError("Missing dataset column: " + column)

    # Handle missing values
    movies["Series_Title"] = movies["Series_Title"].fillna("Unknown")
    movies["Genre"] = movies["Genre"].fillna("")
    movies["Overview"] = movies["Overview"].fillna("")

    # Convert ratings into numbers
    movies["IMDB_Rating"] = pd.to_numeric(
        movies["IMDB_Rating"], errors="coerce"
    )

    # Remove movies without ratings
    movies = movies.dropna(subset=["IMDB_Rating"])

    if movies.empty:
        raise ValueError("The dataset contains no valid movies.")

except FileNotFoundError:
    print(Fore.RED + "Error: imdb_top_1000.csv was not found.")
    print("Place the CSV file in the same folder as this Python program.")
    raise SystemExit

except Exception as error:
    print(Fore.RED + "Dataset Error:", error)
    raise SystemExit


# ==========================================
# 2. PREPARE THE AI RECOMMENDATION MODEL
# ==========================================

# Combine genre and overview for better recommendations
movies["Features"] = (
    movies["Genre"] + " " + movies["Overview"]
)

# Convert movie descriptions into numerical features
tfidf = TfidfVectorizer(stop_words="english")

tfidf_matrix = tfidf.fit_transform(movies["Features"])

# Calculate similarity between movies
similarity_matrix = cosine_similarity(tfidf_matrix)


# ==========================================
# 3. DISPLAY MOVIE DETAILS
# ==========================================

def display_movie(movie):

    print(Fore.CYAN + Style.BRIGHT)
    print("\n========== MOVIE DETAILS ==========")

    print(Fore.YELLOW + "Title: " + str(movie["Series_Title"]))

    print(Fore.GREEN + "Genre: " + str(movie["Genre"]))

    print(Fore.GREEN + "IMDb Rating: " + str(movie["IMDB_Rating"]) + "/10")

    print(Fore.CYAN + "\nOverview:")
    print(movie["Overview"])

    # Sentiment analysis using TextBlob
    sentiment = TextBlob(str(movie["Overview"])).sentiment.polarity

    if sentiment > 0:
        print(Fore.GREEN + "\nSentiment: Positive")

    elif sentiment < 0:
        print(Fore.RED + "\nSentiment: Negative")

    else:
        print(Fore.YELLOW + "\nSentiment: Neutral")

    print(Fore.CYAN + "===================================")


# ==========================================
# 4. RANDOM MOVIE RECOMMENDATION
# ==========================================

def random_recommendation():

    movie = movies.sample(1).iloc[0]

    print(Fore.MAGENTA + "\nYour random movie recommendation:")

    display_movie(movie)


# ==========================================
# 5. AI-BASED MOVIE RECOMMENDATION
# ==========================================

def ai_recommendation():

    print(Fore.CYAN + "\n========== AI RECOMMENDATION ==========")

    genre = input(
        Fore.YELLOW + "Enter your preferred genre: "
    ).strip()

    # Available mood options
    moods = {
        "1": "happy cheerful funny comedy",
        "2": "exciting action adventure thrilling",
        "3": "love romance relationship emotional",
        "4": "mystery suspense investigation discovery",
        "5": "horror scary frightening terrifying",
        "6": "sad tragic emotional drama"
    }

    print(Fore.CYAN + "\nChoose your mood:")
    print("1. Happy")
    print("2. Excited")
    print("3. Romantic")
    print("4. Curious")
    print("5. Scared")
    print("6. Sad")

    mood = input(Fore.YELLOW + "\nEnter your choice (1-6): ").strip()

    if mood not in moods:
        print(Fore.RED + "Invalid mood selection!")
        return

    # Get minimum IMDb rating
    try:
        rating = float(
            input(Fore.YELLOW + "\nMinimum IMDb rating (0-10): ")
        )

        if rating < 0 or rating > 10:
            print(Fore.RED + "Rating must be between 0 and 10.")
            return

    except ValueError:
        print(Fore.RED + "Please enter a valid number.")
        return

    # Filter movies by genre and rating
    filtered_movies = movies[
        (movies["Genre"].str.contains(
            genre, case=False, na=False, regex=False
        )) &
        (movies["IMDB_Rating"] >= rating)
    ]

    if filtered_movies.empty:
        print(Fore.RED + "\nNo movies match your preferences.")
        return

    # Convert the selected mood into TF-IDF features
    mood_vector = tfidf.transform([moods[mood]])

    # Find similarity with filtered movies
    filtered_indices = filtered_movies.index.tolist()

    similarities = cosine_similarity(
        mood_vector,
        tfidf_matrix[filtered_indices]
    )[0]

    # Find the movie with the highest similarity
    best_position = similarities.argmax()

    selected_movie_index = filtered_indices[best_position]

    selected_movie = movies.loc[selected_movie_index]

    print(Fore.MAGENTA + "\nYour AI-based recommendation:")

    display_movie(selected_movie)


# ==========================================
# 6. MAIN PROGRAM
# ==========================================

def main():

    print(Fore.CYAN + Style.BRIGHT)
    print("======================================")
    print("     AI MOVIE RECOMMENDATION SYSTEM")
    print("======================================")

    name = input(Fore.YELLOW + "\nEnter your name: ").strip()

    if not name:
        name = "Movie Lover"

    print(Fore.GREEN + f"\nWelcome, {name}!")

    # Repeat recommendation process
    while True:

        print(Fore.CYAN + "\n========== MAIN MENU ==========")

        print(Fore.GREEN + "1. AI-based Recommendation")
        print(Fore.GREEN + "2. Random Recommendation")
        print(Fore.RED + "3. Exit")

        choice = input(
            Fore.YELLOW + "\nChoose an option (1-3): "
        ).strip()

        if choice == "1":

            ai_recommendation()

        elif choice == "2":

            random_recommendation()

        elif choice == "3":

            print(Fore.CYAN + f"\nGoodbye, {name}! Enjoy your movies!")
            break

        else:

            print(Fore.RED + "Invalid choice. Please select 1, 2, or 3.")

            continue

        # Ask whether the user wants another recommendation
        again = input(
            Fore.YELLOW + "\nWould you like another recommendation? (yes/no): "
        ).strip().lower()

        if again in ["no", "n"]:
            print(Fore.CYAN + "\nThank you for using MovieBot. Goodbye!")
            break

        elif again not in ["yes", "y"]:
            print(Fore.RED + "Invalid response. Returning to the main menu.")


# ==========================================
# 7. RUN THE PROGRAM
# ==========================================

if __name__ == "__main__":
    main()
