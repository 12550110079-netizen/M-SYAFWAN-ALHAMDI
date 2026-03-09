import unittest

class Book:
    def __init__(self, id, title, author, year):
        self.id = id
        self.title = title
        self.author = author
        self.year = year

    def get_summary(self):
        return f"{self.title} by {self.author} ({self.year})"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book_id):
        self.books = [b for b in self.books if b.id != book_id]

    def find_book(self, book_id):
        for book in self.books:
            if book.id == book_id:
                return book
        return None


# UNIT TEST
class TestLibrary(unittest.TestCase):

    def test_add_book(self):
        lib = Library()
        book = Book(1, "Python", "John", 2022)

        lib.add_book(book)

        self.assertEqual(len(lib.books), 1)

    def test_find_book(self):
        lib = Library()
        book = Book(1, "Python", "John", 2022)

        lib.add_book(book)
        result = lib.find_book(1)

        self.assertEqual(result.title, "Python") # pyright: ignore[reportOptionalMemberAccess]


if __name__ == "__main__":
    unittest.main()