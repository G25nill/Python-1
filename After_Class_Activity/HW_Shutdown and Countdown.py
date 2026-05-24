# Code 1 (Shutdown)
'''
# Function to check shutdown condition

def shutdown(answer):
    if answer == "Yes":
        print("Shutting down")
        
    elif answer == "No":
        print("Abort shut down")
        
    else:
        print("Sorry")

# Take input from user
user_input = input("Enter Yes or No: ")

# Call the function
shutdown(user_input)
'''

# Code 2 (Countdown )

# Countdown using recursive function

def countdown(n):
    print(n)
    
    if n == 0:
        print("Done")
    else:
        countdown(n - 1)

# Take input from user
num = int(input("Enter a number: "))

# Call the function
countdown(num)