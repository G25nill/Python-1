def due_amount():
    bill = float(input("Enter the bill amount: "))
    paid = float(input("Enter the amount paid: "))

    return paid - bill

print("Due Amount =", due_amount())