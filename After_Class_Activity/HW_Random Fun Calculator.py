# Random Fun Calculator

# Import the required modules
import random
import math


print("===== RANDOM FUN CALCULATOR =====")


# Generate and display a lucky number
lucky_num = random.randint(1, 10)
print("Your lucky number is:", lucky_num)


# Select a random activity
activities = ["Play a game","Solve a puzzle","Read a story","Draw something"]

today_activity = random.choice(activities)
print("Random activity for today:", today_activity)


# Number guessing game
print("\nGuess the secret number from 1 to 5!")

hidden_number = random.randint(1, 5)

while True:
    user_guess = int(input("Enter your guess: "))

    if user_guess == hidden_number:
        print("Correct! You guessed the number.")
        break
    else:
        print("Wrong guess. Try again!")


# Find the ceiling and floor values
number = float(input("\nEnter a decimal number: "))

ceiling_result = math.ceil(number)
floor_result = math.floor(number)

print("Ceiling value:", ceiling_result)
print("Floor value:", floor_result)


# Copy the sign of one number to another
first_number = 10
second_number = -5

sign_result = math.copysign(first_number, second_number)

print("Copy sign result:", sign_result)


# Find the absolute value
number_to_check = int(input("Enter a negative number: "))

absolute_result = math.fabs(number_to_check)

print("Absolute value:", absolute_result)


# Find the greatest common divisor
first_gcd_number = int(input("Enter first number for GCD: "))
second_gcd_number = int(input("Enter second number for GCD: "))

gcd_result = math.gcd(first_gcd_number, second_gcd_number)

print("GCD is:", gcd_result)


# Display the final summary
print("\n===== FUN CALCULATOR SUMMARY =====")
print("Lucky Number:", lucky_num)
print("Random Activity:", today_activity)
print("Secret Number:", hidden_number)
print("==================================")