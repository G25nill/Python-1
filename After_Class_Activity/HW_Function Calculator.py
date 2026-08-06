def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


print("Function Calculator")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

try:
    choice = int(input("Enter your choice (1-4): "))

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == 1:
        answer = add(num1, num2)
        print("Result =", answer)

    elif choice == 2:
        answer = subtract(num1, num2)
        print("Result =", answer)

    elif choice == 3:
        answer = multiply(num1, num2)
        print("Result =", answer)

    elif choice == 4:
        answer = divide(num1, num2)
        print("Result =", answer)

    else:
        print("Invalid choice.")

except ValueError:
    print("Error: Please enter numbers only.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")