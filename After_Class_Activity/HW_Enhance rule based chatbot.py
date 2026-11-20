
import re
import random
from datetime import datetime
from zoneinfo import ZoneInfo
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Destination data
destinations = {
    "beaches": ["Bali", "Maldives", "Phuket"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
    "cities": ["Tokyo", "Paris", "New York"]
}

# Joke data
jokes = [
    "Why don't programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do travelers always feel warm? Because of all their hot spots!"
]

# Simulated weather information
weather_data = {
    "dhaka": "Sunny, 30°C",
    "tokyo": "Cloudy, 18°C",
    "paris": "Rainy, 15°C",
    "bali": "Sunny, 29°C",
    "london": "Windy, 12°C"
}

# Simulated news updates
news = [
    "A new international airport has opened in a major tourist destination!",
    "Several countries have announced new tourism campaigns.",
    "Airlines are introducing new routes for international travelers."
]

# Time zones of different cities
time_zones = {
    "dhaka": "Asia/Dhaka",
    "tokyo": "Asia/Tokyo",
    "paris": "Europe/Paris",
    "london": "Europe/London",
    "new york": "America/New_York"
}

# Conversation memory
conversation_history = []

# Normalize user input
def normalize_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())


# Check keywords using lists
def matches_keyword(text, keywords):
    return any(re.search(r"\b" + re.escape(word) + r"\b", text)
               for word in keywords)


# Travel recommendations
def recommend():
    print(Fore.CYAN + "\nTravelBot: Beaches, mountains, or cities?")
    preference = normalize_input(input(Fore.YELLOW + "You: "))

    if preference in destinations:
        suggestion = random.choice(destinations[preference])

        print(Fore.GREEN + f"TravelBot: How about {suggestion}?")
        answer = normalize_input(input(Fore.YELLOW + "You (yes/no): "))

        while answer not in ["yes", "y", "no", "n"]:
            print(Fore.RED + "Please answer yes or no.")
            answer = normalize_input(input(Fore.YELLOW + "You: "))

        if answer in ["yes", "y"]:
            print(Fore.GREEN + f"Awesome! Enjoy {suggestion}!")
        else:
            print(Fore.CYAN + "Let's try another destination!")
            recommend()

    else:
        print(Fore.RED + "Sorry, I don't have that type of destination.")
        recommend()


# Packing tips
def packing_tips():
    location = input(Fore.YELLOW + "\nTravelBot: Where are you going? ")
    location = normalize_input(location)

    days = input(Fore.YELLOW + "TravelBot: How many days? ")

    while not days.isdigit() or int(days) <= 0:
        print(Fore.RED + "Please enter a valid number of days.")
        days = input(Fore.YELLOW + "You: ")

    print(Fore.GREEN + f"\nPacking tips for {days} days in {location}:")
    print(Fore.GREEN + "- Pack versatile clothes.")
    print(Fore.GREEN + "- Bring chargers and adapters.")
    print(Fore.GREEN + "- Check the weather forecast.")
    print(Fore.GREEN + "- Carry essential travel documents.")
    print(Fore.GREEN + "- Pack enough personal items.")


# Tell a random joke
def tell_joke():
    print(Fore.YELLOW + "\nTravelBot: " + random.choice(jokes))


# New Feature 1: Weather information
def check_weather():
    city = normalize_input(input(Fore.YELLOW + "\nTravelBot: Which city's weather? "))

    if city in weather_data:
        print(Fore.GREEN + f"TravelBot: Weather in {city.title()}: {weather_data[city]}")
    else:
        print(Fore.RED + "Sorry, weather information is unavailable for that city.")


# New Feature 2: News updates
def show_news():
    print(Fore.CYAN + "\nTravelBot: Here are some travel news updates:")

    for i, story in enumerate(news, 1):
        print(Fore.GREEN + f"{i}. {story}")


# New Feature 3: Local time
def check_time():
    city = normalize_input(input(Fore.YELLOW + "\nTravelBot: Which city's time do you want? "))

    if city in time_zones:
        current_time = datetime.now(ZoneInfo(time_zones[city]))
        print(Fore.GREEN + f"TravelBot: Current time in {city.title()}: "
              f"{current_time.strftime('%I:%M %p, %d %B %Y')}")
    else:
        print(Fore.RED + "Sorry, I don't have the time zone for that city.")


# Display help menu
def show_help():
    print(Fore.MAGENTA + Style.BRIGHT + "\n===== TRAVELBOT HELP MENU =====")

    print(Fore.GREEN + "- Suggest travel spots (recommendation / suggest)")
    print(Fore.GREEN + "- Offer packing tips (packing / pack)")
    print(Fore.GREEN + "- Tell a joke (joke / funny)")
    print(Fore.GREEN + "- Check simulated weather (weather)")
    print(Fore.GREEN + "- Read travel news (news)")
    print(Fore.GREEN + "- Check local time (time)")
    print(Fore.GREEN + "- Display help menu (help)")

    print(Fore.CYAN + "Type 'exit' or 'bye' to end the conversation.\n")


# Main chatbot loop
def chat():
    print(Fore.CYAN + Style.BRIGHT + "Hello! I'm TravelBot.")

    name = input(Fore.YELLOW + "What is your name? ")
    print(Fore.GREEN + f"Nice to meet you, {name}!")

    show_help()

    while True:
        user_input = normalize_input(input(Fore.YELLOW + f"\n{name}: "))

        # Save conversation in memory
        conversation_history.append(user_input)

        # Exit
        if matches_keyword(user_input, ["exit", "bye", "goodbye", "quit"]):
            print(Fore.CYAN + "TravelBot: Safe travels! Goodbye!")
            break

        # Travel recommendations
        elif matches_keyword(user_input, ["recommendation", "recommend", "suggest", "destination"]):
            recommend()

        # Packing tips
        elif matches_keyword(user_input, ["pack", "packing", "luggage"]):
            packing_tips()

        # Jokes
        elif matches_keyword(user_input, ["joke", "funny", "humor"]):
            tell_joke()

        # Weather
        elif matches_keyword(user_input, ["weather", "temperature", "forecast"]):
            check_weather()

        # News
        elif matches_keyword(user_input, ["news", "updates", "headlines"]):
            show_news()

        # Local time
        elif matches_keyword(user_input, ["time", "clock"]):
            check_time()

        # Help
        elif matches_keyword(user_input, ["help", "commands", "options"]):
            show_help()

        # Memory feature
        elif "history" in user_input or "remember" in user_input:
            print(Fore.MAGENTA + "TravelBot: Your previous inputs:")
            for item in conversation_history[:-1]:
                print(Fore.GREEN + "- " + item)

        else:
            print(Fore.RED + "TravelBot: Sorry, I didn't understand. Type 'help' to see my features.")


# Run the chatbot
if __name__ == "__main__":
    chat()
