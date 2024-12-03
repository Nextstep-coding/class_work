"""
Welcome to the Little Python Library!

Our librarian, Alex, needs some help managing the library's data.
Below is a series of tasks that Alex needs to complete. Your job is to implement
the required functionality using Python lists, dictionaries, and sets.
"""

# Step 1: A list of all available books
# TODO: Create a list named `books` that contains the following titles:
# "The Great Gatsby", "To Kill a Mockingbird", "1984", "Pride and Prejudice", "The Catcher in the Rye"

books = []  # Replace with your list of books
print("List of books in the library:")
print(books)

# Step 2: Record borrowed books
# Alex wants to track which books have been borrowed and who borrowed them.
# TODO: Create a dictionary named `borrowed_books`. Each key should be a book title,
# and the value should be the name of the borrower. For now, only the following two entries are needed:
# - "1984" is borrowed by "Alice"
# - "The Great Gatsby" is borrowed by "Bob"

borrowed_books = {}  # Replace with your dictionary
print("\nBorrowed books and their borrowers:")
print(borrowed_books)

# Step 3: Find unique borrowers
# Sometimes people borrow multiple books. Alex needs to find out who borrowed books without duplication.
# TODO: Use a set to store the names of all borrowers.

borrowers = set()  # Replace with a set of unique borrower names
print("\nUnique borrowers:")
print(borrowers)

# Step 4: Adding new books
# The library has received some new books! Alex wants to add them to the collection.
# TODO: Extend the `books` list by adding "Moby Dick" and "War and Peace".

# Add the new books here

print("\nUpdated list of books:")
print(books)

# Step 5: Checking availability
# Alex wants to create a function that checks if a book is available in the library.
# TODO: Implement the `is_book_available` function. It should return True if the book is not borrowed,
# and False otherwise.

def is_book_available(book_title):
    # Replace with your implementation
    pass

# Test the function
print("\nIs '1984' available?", is_book_available("1984"))
print("Is 'To Kill a Mockingbird' available?", is_book_available("To Kill a Mockingbird"))

# Step 6: Returning a book
# Alex needs to update the borrowed books when someone returns a book.
# TODO: Write a function `return_book` that takes the title of the returned book and updates `borrowed_books`.

def return_book(book_title):
    # Replace with your implementation
    pass

# Test the return_book function
return_book("1984")
print("\nBorrowed books after returning '1984':")
print(borrowed_books)

# Step 7: Summary of available books
# TODO: Create a set of books that are currently available (not borrowed). Use set operations to determine this.

available_books = set()  # Replace with a set of available books
print("\nBooks available in the library:")
print(available_books)

"""
Great work! You've successfully helped Alex manage the library. 🎉
"""

