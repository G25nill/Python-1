class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if self.is_borrowed:
            print("This book is already borrowed.")
        else:
            self.is_borrowed = True
            print(self.title, "has been borrowed.")

    def return_book(self):
        if not self.is_borrowed:
            print("This book was not borrowed.")
        else:
            self.is_borrowed = False
            print(self.title, "has been returned.")

    def __str__(self):
        if self.is_borrowed:
            status = "Borrowed"
        else:
            status = "Available"

        return self.title + " by " + self.author + " [" + status + "]"


# Creating some books
book1 = Book("The Hobbit", "J.R.R. Tolkien")
book2 = Book("Harry Potter", "J.K. Rowling")
book3 = Book("Animal Farm", "George Orwell")

print("=" * 42)
print("          LIBRARY SYSTEM")
print("=" * 42)

# Displaying the books
print(book1)
print(book2)
print(book3)

print("\nBorrowing books:")
book1.borrow()
book2.borrow()

# Trying to borrow an already borrowed book
book1.borrow()

print("\nReturning books:")
book1.return_book()

# Trying to return a book that is available
book3.return_book()

print("\nUpdated library:")
print(book1)
print(book2)
print(book3)

