# Function to calculate circumference of a circle

def circumference(radius):
    result = 2 * 3.14 * radius
    return result

# Take input from user
r = float(input("Enter the radius: "))

# Call the function
answer = circumference(r)

# Print the result
print("Circumference of the circle is:", answer)