class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book Added")

    def issue_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print("Book Issued")
        else:
            print("Book Not Available")

    def return_book(self, book):
        self.books.append(book)
        print("Book Returned")

    def display_books(self):
        print("Available Books:", self.books)

library = Library()

library.add_book("Python")
library.add_book("Java")

library.display_books()

library.issue_book("Python")

library.display_books()

library.return_book("Python")

library.display_books()