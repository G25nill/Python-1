# ASCII Value Checker

char = input("Enter a single character: ")

# Check if only one character is entered
if len(char) == 1:

    print("Character:", char)
    print("ASCII Value:", ord(char))

    # Identify type of character
    if char >= 'A' and char <= 'Z':
        print("Character Type: Uppercase Letter")

    elif char >= 'a' and char <= 'z':
        print("Character Type: Lowercase Letter")

    elif char >= '0' and char <= '9':
        print("Character Type: Digit")

    else:
        print("Character Type: Special Character")

else:
    print("Error: Please enter exactly one character.")