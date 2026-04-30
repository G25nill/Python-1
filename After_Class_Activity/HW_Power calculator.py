# program to find power of a number

num = int(input("Enter a number: "))
power = int(input("Enter the power: "))

result = 1

for i in range(power):
    result = result * num

print("The answer is:", result)