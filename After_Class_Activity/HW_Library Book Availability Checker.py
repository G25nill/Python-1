# PART 1: Store the book titles and their copy quantities
book_list = ["matilda", "harry potter", "wonder", "the jungle book", "charlie"]
copies = [4, 0, 6, 3, 2]

# PART 2: Create the library dictionary using zip()
stock = {title: amount for title, amount in zip(book_list, copies)}
print("Full Library Stock:", stock)

# PART 3: Make a list containing only books with copies available
books_in_stock = [title for title in book_list if stock[title] > 0]
print("Books Available:", books_in_stock)

# PART 4: Get the book the reader wants to borrow
selected_book = input("Which book do you want to borrow? ")

# PART 5: End the program if the selected book cannot be borrowed
if selected_book not in stock or stock[selected_book] == 0:
    print(selected_book, "is not available! Stopping the checker.")
    exit()

# PART 6: Store the original late fees and get an additional fee
fees = [5, 8, 4, 6, 7]
additional_fee = int(input("Enter the extra library fee to add to every book: "))

# PART 7: Add the extra fee to each late fee using map()
new_fees = list(map(lambda x: x + additional_fee, fees))
print("Updated Late Fees:", new_fees)

# PART 8: Locate the selected book and get its updated late fee
selected_index = book_list.index(selected_book)
final_fee = new_fees[selected_index]
print("Late fee for", selected_book, "after update:", final_fee)

# PART 9: Decrease the number of available copies by one
stock[selected_book] -= 1
print(selected_book, "borrowed! Remaining copies:", stock[selected_book])

# PART 10: Display the final results
print("")
print("===== LIBRARY BOOK AVAILABILITY CHECKER =====")
print("Book Borrowed:", selected_book)
print("Late Fee:", final_fee)
print("Updated Library Stock:", stock)
print("=============================================")