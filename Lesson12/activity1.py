#Take input
print("Hald Pyramid Pattern of Stars (*):")
n = int(input("enter the number of rows: "))
#outer loop to handel of rows
for i in range(n):
    #inner loop to handle number of columns
    for j in range(i+1):
        #display result
        print("* ", end="")
    print()