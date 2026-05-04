# take input from user
num = int(input("Enter a number: "))

# store original number
original = num

# variables
count = 0
reverse = 0

# first loop: count digits
temp = num
while temp > 0:
    temp = temp // 10
    count = count + 1

print("Total digits:", count)

# second loop: reverse number and Armstrong check
temp = num
armstrong_sum = 0

while temp > 0:
    digit = temp % 10
    
    # reverse number
    reverse = reverse * 10 + digit
    
    # armstrong calculation
    armstrong_sum = armstrong_sum + (digit ** count)
    
    temp = temp // 10

print("Reversed number:", reverse)

# check armstrong
if armstrong_sum == original:
    print("It is an Armstrong number")
else:
    print("It is NOT an Armstrong number")