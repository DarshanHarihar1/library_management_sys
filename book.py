class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.books = []

    def add_books_db(self):
        return [self.title, self.author, self.isbn]

