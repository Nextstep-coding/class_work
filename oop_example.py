# class Book:
#     """A class to represent a book in the library."""
#
#     def __init__(self, title, author, copies):
#         self.title = title
#         self.author = author
#         self.copies = copies
#
#     def display_info(self):
#         """Displays details about the book."""
#         print(f"Title: {self.title}, Author: {self.author}, Copies Available: {self.copies}")
#
#     def borrow_book(self):
#         """Decreases the number of copies when a book is borrowed."""
#         if self.copies > 0:
#             self.copies -= 1
#             print(f"You've borrowed '{self.title}'. Copies left: {self.copies}")
#         else:
#             print(f"Sorry, '{self.title}' is out of stock!")
#
#     def return_book(self):
#         """Increases the number of copies when a book is returned."""
#         self.copies += 1
#         print(f"Thanks for returning '{self.title}'. Copies now: {self.copies}")
#
#
# class Library:
#     """A class to represent the library."""
#
#     def __init__(self, name):
#         self.name = name
#         self.catalog = []
#
#     def add_book(self, book):
#         """Adds a book to the library catalog."""
#         self.catalog.append(book)
#         print(f"'{book.title}' has been added to the library!")
#
#     def show_catalog(self):
#         """Displays all the books in the catalog."""
#         print(f"\nLibrary: {self.name}")
#         if not self.catalog:
#             print("No books available.")
#         else:
#             for idx, book in enumerate(self.catalog, 1):
#                 print(f"{idx}. ", end="")
#                 book.display_info()
#
#
# class Member:
#     """A class to represent a library member."""
#
#     def __init__(self, name):
#         self.name = name
#
#     def borrow(self, library, book_title):
#         """Allows a member to borrow a book from the library."""
#         for book in library.catalog:
#             if book.title == book_title:
#                 book.borrow_book()
#                 return
#         print(f"Sorry, '{book_title}' is not available in the library.")
#
#     def return_book(self, library, book_title):
#         """Allows a member to return a book to the library."""
#         for book in library.catalog:
#             if book.title == book_title:
#                 book.return_book()
#                 return
#         print(f"'{book_title}' does not belong to this library.")
#
#
# # Demonstration of OOP Concepts
# if __name__ == "__main__":
#     # Creating a Library
#     my_library = Library("City Library")
#
#     # Creating Books
#     book1 = Book("Python Programming", "John Doe", 3)
#     book2 = Book("Data Science Essentials", "Jane Smith", 2)
#
#     # Adding Books to the Library
#     my_library.add_book(book1)
#     my_library.add_book(book2)
#
#     # Display the Catalog
#     my_library.show_catalog()
#
#     # Creating a Library Member
#     member = Member("Alice")
#
#     # Borrowing Books
#     member.borrow(my_library, "Python Programming")
#     member.borrow(my_library, "Python Programming")
#     member.borrow(my_library, "Python Programming")
#     member.borrow(my_library, "Python Programming")  # Attempting to borrow when out of stock
#
#     # Returning a Book
#     member.return_book(my_library, "Python Programming")
#
#     # Display the Updated Catalog
#     my_library.show_catalog()

class Student:
    def __init__(self, first_name, last_name,gender,grade,age):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
        self.grade = grade
    def ask_question(slef, q):
        print(f"{slef.first_name} asked :{q}")

hekmat = Student('Hekmat','dalati','male','12','18')
jj = Student('jihu','jang','male','11','16')
hekmat.ask_question('where?')
jj.ask_question('why?')