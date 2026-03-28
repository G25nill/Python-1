
# Program 1: Student Marks Square Root

marks = float(input("Enter your marks: "))

if marks >= 0:
    result = marks ** 0.5
    print("Square root of your marks is:", result)
else:
    print("Invalid marks entered")


# -------------------------------------------
# Program 2: Student Performance Checker

score = int(input("\nEnter your exam score: "))

# Using > and <
if score > 0 and score < 50:
    print("Needs improvement")

# Using >= and <=
elif score >= 50 and score <= 80:
    print("Good performance")

elif score > 80 and score <= 100:
    print("Excellent performance")

# Using ==
elif score == 0:
    print("You scored zero")

# Using !=
if score != 75:
    print("Score is not equal to 75")
else:
    print("You got exactly 75")