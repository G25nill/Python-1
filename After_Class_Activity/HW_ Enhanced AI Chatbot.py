
# Enhanced AI Chatbot

# Greet the user
print("Hello! Welcome to my chatbot.")
name = input("What is your name? ")

print("Nice to meet you, " + name + "!")

# Start the conversation
while True:

    # Ask about the user's mood
    mood = input("\nHow are you feeling today? (good/bad/neutral): ").lower()

    # Respond according to the mood
    if mood == "good":
        print("That's wonderful! I'm happy to hear that.")

    elif mood == "bad":
        print("I'm sorry to hear that. I hope your day gets better!")

    elif mood == "neutral":
        print("That's okay! I hope something exciting happens today.")

    else:
        print("I don't understand your mood, but I hope you're doing well!")

    # Ask about hobbies
    hobby = input("\nWhat is your favourite hobby? ").lower()
    print("That's interesting! I hope you enjoy " + hobby + ".")

    # Ask about favourite activities
    activity = input("\nWhat do you like to do in your free time? ")
    print("That sounds fun, " + name + "!")

    # Ask whether the user wants to continue
    choice = input("\nWould you like to chat again? (yes/no): ").lower()

    if choice == "no":
        print("\nIt was nice talking to you, " + name + "!")
        print("Goodbye! Have a great day!")
        break

    elif choice == "yes":
        print("\nGreat! Let's continue chatting.")

    else:
        print("\nI didn't understand that. Let's start another conversation!")
