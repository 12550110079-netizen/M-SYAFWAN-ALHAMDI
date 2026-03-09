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