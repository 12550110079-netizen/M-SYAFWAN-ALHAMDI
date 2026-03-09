class Book:
    def __init__(self, title, author, year, price):
        self.title = title
        self.author = author
        self.year = year
        self.price = price

    def get_info(self):
        return f"{self.title} by {self.author} ({self.year}) - Rp{self.price}"

    def apply_discount(self, discount):
        self.price = self.price - (self.price * discount)


if __name__ == "__main__":
    book1 = Book("Python Basics", "John Doe", 2022, 150000)

    print(book1.get_info())

    book1.apply_discount(0.1)

    print("Harga setelah diskon:", book1.price)
  