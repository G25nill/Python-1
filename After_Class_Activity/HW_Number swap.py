# Input three numbers
A = int(input("Enter A: "))
B = int(input("Enter B: "))
C = int(input("Enter C: "))

# Swapping
TEMP = A
A = B
B = C
C = TEMP

# Output result
print("After swapping:")
print("A =", A)
print("B =", B)
print("C =", C)