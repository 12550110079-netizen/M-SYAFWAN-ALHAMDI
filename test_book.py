import unittest
from book import Book # pyright: ignore[reportMissingImports]

class TestBook(unittest.TestCase):

    def test_book_creation(self):
        book = Book("Python", "John", 2022, 100000)
        self.assertEqual(book.title, "Python")
        self.assertEqual(book.author, "John")

    def test_discount(self):
        book = Book("Python", "John", 2022, 100000)
        book.apply_discount(0.1)
        self.assertEqual(book.price, 90000)

if __name__ == "__main__":
    unittest.main()