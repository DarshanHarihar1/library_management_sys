class BookManager:
    def __init__(self):
        self.books = []

    def add_books(self, book):
        self.books.append(book)

    def remove_books(self, book):
        self.books.remove(book)

    def search_books(self, attribute, value):
        return [book for book in self.books if getattr(book, attribute) == value]

    def list_books(self):
        return self.books

    def update_book(self, old_title, new_title, new_author, new_isbn):
        for book in self.books:
            if book.title == old_title:
                book.title = new_title
                book.author = new_author
                book.isbn = new_isbn
                return True
        return False

class UserManager:
    def __init__(self):
        self.users = []

    def add_users(self, user):
        self.users.append(user)

    def remove_users(self, user):
        self.users.remove(user)

    def search_users(self, attribute, value):
        return [user for user in self.users if getattr(user, attribute) == value]

    def list_users(self):
        return self.users

    def update_user(self, old_user_id, new_name, new_user_id):
        for user in self.users:
            if user.user_id == old_user_id:
                user.name = new_name
                user.user_id = new_user_id
                return True
        return False

    def update_user_data(self, user_id, new_name, new_user_id):
        for user in self.users:
            if user.user_id == user_id:
                user.name = new_name
                user.user_id = new_user_id
                return True
        return False

