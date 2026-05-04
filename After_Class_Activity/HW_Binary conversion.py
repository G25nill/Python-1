num = int(input("Enter a decimal number: "))

binary = ""
temp = num

while temp > 0:
    remainder = temp % 2
    
    # inner loop (runs once, just to show nesting)
    i = 0
    while i < 1:
        binary = str(remainder) + binary
        i += 1
    
    temp //= 2

print("Binary number:", binary)