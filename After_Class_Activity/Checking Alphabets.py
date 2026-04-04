# Take input
text = input("Enter characters: ")

# Check each character
for characters in text:
    if characters.isalpha():
        print(characters, "-> Alphabet")
    elif characters.isdigit():
        print(characters, "-> Digit")
    else:
        print(characters, "-> Special Character")