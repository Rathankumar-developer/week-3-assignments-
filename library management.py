"""
Week 3 - Assignment 2: Library Management System (OOP)
Add/remove books, issue/return books.
"""


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_issued = False


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        self.books.append(Book(title, author))
        print(f"Added book: '{title}' by {author}")

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"Removed book: '{title}'")
                return
        print(f"Book '{title}' not found.")

    def issue_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.is_issued:
                    print(f"'{title}' is already issued.")
                else:
                    book.is_issued = True
                    print(f"Issued: '{title}'")
                return
        print(f"Book '{title}' not found.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                if not book.is_issued:
                    print(f"'{title}' was not issued.")
                else:
                    book.is_issued = False
                    print(f"Returned: '{title}'")
                return
        print(f"Book '{title}' not found.")

    def display_books(self):
        print("\nLibrary Catalog:")
        if not self.books:
            print("  (no books)")
        for book in self.books:
            status = "Issued" if book.is_issued else "Available"
            print(f"  '{book.title}' by {book.author} - {status}")
        print()


if __name__ == "__main__":
    lib = Library()
    lib.add_book("The Hobbit", "J.R.R. Tolkien")
    lib.add_book("1984", "George Orwell")
    lib.display_books()

    lib.issue_book("1984")
    lib.issue_book("1984")     # already issued
    lib.display_books()

    lib.return_book("1984")
    lib.remove_book("The Hobbit")
    lib.display_books()
