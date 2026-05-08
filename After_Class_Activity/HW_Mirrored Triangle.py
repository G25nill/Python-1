#Take input
print("Mirrored Right-Angled Triangle Pattern of Stars (*)")
n = int(input("Enter the number of rows: "))

#outer loop to handle rows
for i in range(n):
    
    #inner loop for spaces
    for j in range(n - i - 1):
        print("  ", end="")
    
    #inner loop for stars
    for j in range(i + 1):
        print("* ", end="")
    
    #move to next line
    print()