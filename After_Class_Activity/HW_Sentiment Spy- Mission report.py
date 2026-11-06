
# Sentiment Spy: Mission Report

# Import necessary libraries
from textblob import TextBlob
from colorama import Fore, init
import time
import sys

# Initialize Colorama
init(autoreset=True)

# Store sentiment counts
positive_count = 0
negative_count = 0
neutral_count = 0

# Store conversation history
conversation_history = []


# Function to display processing animation
def show_processing_animation():
    print("Analyzing your message", end="")

    for i in range(3):
        print(".", end="")
        sys.stdout.flush()
        time.sleep(0.5)

    print()


# Function to analyze sentiment
def analyze_sentiment(text):

    global positive_count, negative_count, neutral_count

    # Calculate polarity using TextBlob
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    # Classify the sentiment
    if polarity > 0.25:
        sentiment = "Positive"
        positive_count += 1
        color = Fore.GREEN

    elif polarity < -0.25:
        sentiment = "Negative"
        negative_count += 1
        color = Fore.RED

    else:
        sentiment = "Neutral"
        neutral_count += 1
        color = Fore.YELLOW

    # Display the result
    print(color + "\nSentiment:", sentiment)
    print(color + "Polarity Score:", round(polarity, 2))

    # Display sentiment strength
    if abs(polarity) > 0.75:
        print(color + "Strength: Strong")
    elif abs(polarity) > 0.25:
        print(color + "Strength: Moderate")
    else:
        print(color + "Strength: Neutral")

    # Save message and result in history
    conversation_history.append({
        "message": text,
        "sentiment": sentiment,
        "polarity": round(polarity, 2)
    })


# Function to display sentiment summary
def show_summary():

    print("\n----- SENTIMENT SUMMARY -----")
    print("Positive messages:", positive_count)
    print("Negative messages:", negative_count)
    print("Neutral messages:", neutral_count)


# Function to display conversation history
def show_history():

    print("\n----- CONVERSATION HISTORY -----")

    if len(conversation_history) == 0:
        print("No messages found.")

    else:
        for item in conversation_history:
            print("\nMessage:", item["message"])
            print("Sentiment:", item["sentiment"])
            print("Polarity:", item["polarity"])


# Function to reset stored data
def reset_data():

    global positive_count, negative_count, neutral_count

    positive_count = 0
    negative_count = 0
    neutral_count = 0

    conversation_history.clear()

    print(Fore.YELLOW + "All data has been reset successfully!")


# Function to display available commands
def show_help():

    print("\n----- AVAILABLE COMMANDS -----")
    print("summary - View sentiment statistics")
    print("reset   - Reset all stored data")
    print("history - View previous messages")
    print("help    - View available commands")
    print("exit    - End the chatbot")


# Function to execute commands
def execute_command(command):

    if command == "summary":
        show_summary()

    elif command == "reset":
        reset_data()

    elif command == "history":
        show_history()

    elif command == "help":
        show_help()

    else:
        print(Fore.RED + "Unknown command. Type 'help' for commands.")


# Function to get a valid username
def get_valid_name():

    while True:
        name = input("Enter your name: ").strip()

        if name.isalpha():
            return name

        else:
            print(Fore.RED + "Invalid name. Use alphabetic characters only.")


# Main chatbot program
def main():

    print("=" * 40)
    print(Fore.CYAN + "       SENTIMENT SPY")
    print(Fore.CYAN + "      MISSION REPORT")
    print("=" * 40)

    # Welcome the user
    print("\nWelcome, Agent!")
    username = get_valid_name()

    print(Fore.GREEN + "\nWelcome Agent " + username + "!")
    print("I am Sentiment Spy, your sentiment analysis chatbot.")

    show_help()

    # Main chatbot loop
    while True:

        user_input = input("\nEnter a message or command: ").strip()

        if user_input.lower() == "exit":
            break

        elif user_input.lower() in ["summary", "reset", "history", "help"]:
            execute_command(user_input.lower())

        elif user_input.startswith("/"):
            execute_command(user_input[1:].lower())

        elif user_input == "":
            print(Fore.RED + "Please enter a message.")

        else:
            show_processing_animation()
            analyze_sentiment(user_input)

    # Generate final report
    print("\n" + "=" * 40)
    print(Fore.CYAN + "       FINAL MISSION REPORT")
    print("=" * 40)

    show_summary()

    # Save report to a text file
    filename = username + "_sentiment_analysis.txt"

    with open(filename, "w") as file:
        file.write("SENTIMENT SPY: MISSION REPORT\n")
        file.write("=" * 30 + "\n")
        file.write("Agent Name: " + username + "\n")
        file.write("Positive messages: " + str(positive_count) + "\n")
        file.write("Negative messages: " + str(negative_count) + "\n")
        file.write("Neutral messages: " + str(neutral_count) + "\n")
        file.write("Total messages: " + str(
            positive_count + negative_count + neutral_count
        ) + "\n")

    print(Fore.GREEN + "\nMission completed successfully!")
    print("Report saved as:", filename)


# Run the chatbot
main()
