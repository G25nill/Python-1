actual_cost = float(input(" Please Enter the Actual Product Price:"))
sale_amount = float(input(" Please Enter the Sales Amount:"))

if (sale_amount > actual_cost):
    amount = sale_amount - actual_cost
    print(f"Total Profit = {amount}")
else:
    print("No Profit!!!")