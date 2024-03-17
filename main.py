from model import BookManager, UserManager
from book import Book
from user import User
from storage import save_file, load_file

books = BookManager()
users = UserManager()

def main():
        books_data = load_file('books.csv')
        users_data = load_file('users.csv')

        for book_data in books_data:
            books.add_books(Book(*book_data))

        for user_data in users_data:
            users.add_users(User(*user_data))

        while True:
            print("\nLibrary Management System")
            print("1. Add Book")
            print("2. List All Books")
            print("3. Add User")
            print("4. List All Users")
            print("5. Update Book")
            print("6. Delete Book")
            print("7. Update User")
            print("8. Delete User")
            print("9. Search Book")
            print("10. Search User")
            print("11. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                add_book(books)
            elif choice == '2':
                list_all_books(books)
            elif choice == '3':
                add_user(users)
            elif choice == '4':
                list_all_users(users)
            elif choice == '5':
                update_book_info(books)
            elif choice == '6':
                remove_book(books)
            elif choice == '7':
                update_user_info(users)
            elif choice == '8':
                remove_user(users)
            elif choice == '9':
                search_book(books)
            elif choice == '10':
                search_user(users)
            elif choice == '11':
                break
            else:
                print("Not Valid")


def add_book(books):
        title = input("Enter title: ")
        author = input("Enter author: ")
        isbn = input("Enter ISBN: ")
        book = Book(title, author, isbn)
        books.add_books(book)
        save_file([book.add_books_db() for book in books.list_books()], 'books.csv')
        print("Book added successfully.")



def list_all_books(books):
        all_books = books.list_books()
        if all_books:
            for book in all_books:
                print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}")
        else:
            print("No books in the library.")

        
        
def add_user(users):
        name = input("Enter name: ")
        user_id = input("Enter user ID: ")
        user = User(name, user_id)
        users.add_users(user)
        save_file([user.add_users_db() for user in users.list_users()], 'users.csv')
        print("User added successfully.")

def list_all_users(users):
        all_users = users.list_users()
        if all_users:
            for user in all_users:
                print(f"Name: {user.name}, ID: {user.user_id}")
        else:
            print("No users in the library.")


def update_book_info(books):
        old_title = input("Enter the title of the book to update: ")
        new_title = input("Enter the new title: ")
        new_author = input("Enter the new author: ")
        new_isbn = input("Enter the new ISBN: ")

        if books.update_book(old_title, new_title, new_author, new_isbn):
            print("Book information updated successfully.")
        else:
            print("Book not found.")


def remove_book(books):
        title = input("Enter title of the book to remove: ")
        found_books = books.search_books("title", title)  
        if found_books:
            for i, book in enumerate(found_books):
                print(f"{i + 1}. {book.title} by {book.author}")
            choice = int(input("Enter the number of the book to remove: ")) - 1
            books.remove_books(found_books[choice])
            print("Book removed successfully.")
        else:
            print("Book not found.")


def update_user_info(users):
        old_user_id = input("Enter the ID of the user to update: ")
        new_name = input("Enter the new name: ")
        new_user_id = input("Enter the new user ID: ")

        if users.update_user(old_user_id, new_name, new_user_id):
            print("User information updated successfully.")
        else:
            print("User not found.")

def remove_user(users):
        user_id = input("Enter user ID of the user to remove: ")
        found_users = users.search_users("user_id", user_id)
        if found_users:
            for i, user in enumerate(found_users):
                print(f"{i + 1}. {user.name}, ID: {user.user_id}")
            choice = int(input("Enter the number of the user to remove: ")) - 1
            users.remove_users(found_users[choice])
            print("User removed successfully.")
        else:
            print("User not found.")

def search_book(books):
        attribute = input("Enter search attribute (title/author/isbn): ").lower()
        value = input(f"Enter {attribute}: ")
        found_books = books.search_books(attribute, value)
        if found_books:
            for book in found_books:
                print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}")
        else:
            print("No books found.")

        
def search_user(users):
        attribute = input("Enter search attribute (name/user_id): ").lower()
        value = input(f"Enter {attribute}: ")
        found_users = users.search_users(attribute, value)
        if found_users:
            for user in found_users:
                print(f"Name: {user.name}, ID: {user.user_id}")
        else:
            print("No users found.")

if __name__ == "__main__":
    main()
