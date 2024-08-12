                    #================================================================
                    #===== Module 4: Mini-Project | Library Management System =======
                    #================================================================

# Project Requirements
    # In this project, you will apply Object-Oriented Programming (OOP) principles in Python to develop an advanced Library Management System. This command-line-based application is designed to streamline the management of books and resources within a library. Your mission is to create a robust system that allows users to browse, borrow, return, and explore a collection of books while demonstrating your proficiency in OOP principles and the use of modules.

# Enhanced User Interface (UI) and Menu:
    # Create an improved, user-friendly command-line interface (CLI) for the Library Management System with separate menus for each class of the system.
        #                       Welcome to the Library Management System!
        #     Main Menu:
        #     1. Book Operations
        #     2. User Operations
        #     3. Author Operations
        #     4. Quit
    # Book Operations:
        #                        Book Operations:
        #     1. Add a new book
        #     2. Borrow a book
        #     3. Return a book
        #     4. Search for a book
        #     5. Display all books
    # User Operations:
        #                       User Operations:
        #         1. Add a new user
        #         2. View user details
        #         3. Display all users
    # Author Operations:
        #                       Author Operations:
        #         1. Add a new author
        #         2. View author details
        #         3. Display all authors

# Class Structure:
    # Implement a class structure that represents key entities in the library management system, including:
    # Book: A class representing individual books with attributes such as title, author,  genre, publication date, and availability status.
    # User: A class to represent library users with attributes like name, library ID, and a list of borrowed book titles.
    # Author: A class representing book authors with attributes like name and biography.

# Encapsulation:
    # Apply encapsulation principles by defining private attributes and using getters and setters for necessary data access.

# Modules:
    # Organize your code into modules to promote code organization and maintainability. Create separate modules for classes, user interactions, and error handling.

# Menu Actions:
    # Implement the following actions in response to menu selections using the classes you've created:
        # - Adding a new book with all relevant details.
        # - Allowing users to borrow a book, marking it as "Borrowed."
        # - Allowing users to return a book, marking it as "Available."
        # - Searching for a book by its unique identifier (title) and displaying its details.
        # - Displaying a list of all books with their unique identifiers.
        # - Adding a new user with user details.
        # - Viewing user details.
        # - Displaying a list of all users.
        # - Adding a new author with author details.
        # - Viewing author details.
        # - Displaying a list of all authors.
        # - Quitting the application.

# User Interaction:
    # Utilize the input() function within the appropriate menus to enable users to interact with the CLI and select menu options.
    # Implement input validation using regular expressions (regex) to ensure the correct formatting of user input. (Bonus)

# Error Handling:
    # Implement error handling where applicable using try, except, else, and finally blocks to manage potential issues gracefully, such as incorrect user input or file operations.

#================================================================================================
#=====================================Begin Code=================================================
#================================================================================================
import re

class Book:
    def __init__(self, title, author, genre, publication_date):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__publication_date = publication_date
        self.__availability = True

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_genre(self):
        return self.__genre

    def get_publication_date(self):
        return self.__publication_date

    def is_available(self):
        return self.__availability

    def set_availability(self, availability):
        self.__availability = availability

class User:
    def __init__(self, name, library_id):
        self.__name = name
        self.__library_id = library_id
        self.__borrowed_books = []

    def get_name(self):
        return self.__name

    def get_library_id(self):
        return self.__library_id

    def get_borrowed_books(self):
        return self.__borrowed_books

    def borrow_book(self, book):
        if book.is_available():
            book.set_availability(False)
            self.__borrowed_books.append(book)
            print("Book borrowed successfully.")
        else:
            print("Book not available for borrowing.")

    def return_book(self, book):
        if book in self.__borrowed_books:
            book.set_availability(True)
            self.__borrowed_books.remove(book)
            print("Book returned successfully.")
        else:
            print("Book not borrowed by the user.")

class Author:
    def __init__(self, name, biography):
        self.__name = name
        self.__biography = biography

    def get_name(self):
        return self.__name

    def get_biography(self):
        return self.__biography


class LibraryManagementSystem:
    def __init__(self):
        self.__books = []
        self.__users = []
        self.__authors = []

    def add_book(self, book):
        self.__books.append(book)
        print("Book added successfully.")

    def borrow_book(self, user_name, book_title):
        user = self.__get_user_by_name(user_name)
        if user:
            book = self.__get_book_by_title(book_title)
            if book:
                user.borrow_book(book)
            else:
                print("Book not found.")
        else:
            print("User not found.")

    def return_book(self, user_name, book_title):
        user = self.__get_user_by_name(user_name)
        if user:
            book = self.__get_book_by_title(book_title)
            if book:
                user.return_book(book)
            else:
                print("Book not found.")
        else:
            print("User not found.")

    def search_book(self, book_title):
        book = self.__get_book_by_title(book_title)
        if book:
            print("Book Details:")
            print("Title:", book.get_title())
            print("Author:", book.get_author())
            print("Genre:", book.get_genre())
            print("Publication Date:", book.get_publication_date())
            if book.is_available():
                print("Availability: Available")
            else:
                print("Availability: Borrowed")
        else:
            print("Book not found.")

    def display_all_books(self):
        print("All Books:")
        for book in self.__books:
            print("Title:", book.get_title())
            print("Author:", book.get_author())
            print("Genre:", book.get_genre())
            print("Publication Date:", book.get_publication_date())
            if book.is_available():
                print("Availability: Available")
            else:
                print("Availability: Borrowed")
            print("")

    def add_user(self, user):
        self.__users.append(user)
        print("User added successfully.")

    def view_user_details(self, user_name):
        user = self.__get_user_by_name(user_name)
        if user:
            print("User Details:")
            print("Name:", user.get_name())
            print("Library ID:", user.get_library_id())
            borrowed_books = user.get_borrowed_books()
            if borrowed_books:
                print("Borrowed Books:")
                for book in borrowed_books:
                    print("- Title:", book.get_title())
                    print("  Author:", book.get_author())
            else:
                print("No books borrowed.")
        else:
            print("User not found.")

    def display_all_users(self):
        print("All Users:")
        for user in self.__users:
            print("Name:", user.get_name())
            print("Library ID:", user.get_library_id())
            print("")

    def add_author(self, author):
        self.__authors.append(author)
        print("Author added successfully.")

    def view_author_details(self, author_name):
        author = self.__get_author_by_name(author_name)
        if author:
            print("Author Details:")
            print("Name:", author.get_name())
            print("Biography:", author.get_biography())
        else:
            print("Author not found.")

    def display_all_authors(self):
        print("All Authors:")
        for author in self.__authors:
            print("Name:", author.get_name())
            print("Biography:", author.get_biography())
            print("")

    def __get_user_by_name(self, user_name):
        for user in self.__users:
            if user.get_name() == user_name:
                return user
        return None

    def __get_book_by_title(self, book_title):
        for book in self.__books:
            if book.get_title() == book_title:
                return book
        return None

    def __get_author_by_name(self, author_name):
        for author in self.__authors:
            if author.get_name() == author_name:
                return author
        return None


class LibraryManagementSystemCLI:
    def __init__(self):
        self.__library_management_system = LibraryManagementSystem()

    def display_main_menu(self):
        print("Welcome to the Library Management System!")
        print("Main Menu:")
        print("1. Book Operations")
        print("2. User Operations")
        print("3. Author Operations")
        print("4. Quit")

    def display_book_operations_menu(self):
        print("Book Operations:")
        print("1. Add a new book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Search for a book")
        print("5. Display all books")

    def display_user_operations_menu(self):
        print("User Operations:")
        print("1. Add a new user")
        print("2. View user details")
        print("3. Display all users")

    def display_author_operations_menu(self):
        print("Author Operations:")
        print("1. Add a new author")
        print("2. View author details")
        print("3. Display all authors")

    def run(self):
        while True:
            self.display_main_menu()
            choice = input("Enter your choice (1-4): ")
            if choice == "1":
                self.run_book_operations()
            elif choice == "2":
                self.run_user_operations()
            elif choice == "3":
                self.run_author_operations()
            elif choice == "4":
                print("Thank you for using the Library Management System. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def run_book_operations(self):
        while True:
            self.display_book_operations_menu()
            choice = input("Enter your choice (1-5): ")
            if choice == "1":
                self.add_new_book()
            elif choice == "2":
                self.borrow_book()
            elif choice == "3":
                self.return_book()
            elif choice == "4":
                self.search_book()
            elif choice == "5":
                self.display_all_books()
            else:
                print("Invalid choice. Please try again.")

    def add_new_book(self):
        print("---- Add a New Book ----")
        title = input("Enter the title: ")
        author = input("Enter the author: ")
        genre = input("Enter the genre: ")
        publication_date = input("Enter the publication date: ")

        book = Book(title, author, genre, publication_date)
        self.__library_management_system.add_book(book)

    def borrow_book(self):
        print("---- Borrow a Book ----")
        user_name = input("Enter the user name: ")
        book_title = input("Enter the book title: ")

        self.__library_management_system.borrow_book(user_name, book_title)

    def return_book(self):
        print("---- Return a Book ----")
        user_name = input("Enter the user name: ")
        book_title = input("Enter the book title: ")

        self.__library_management_system.return_book(user_name, book_title)

    def search_book(self):
        print("---- Search for a Book ----")
        book_title = input("Enter the book title: ")

        self.__library_management_system.search_book(book_title)

    def display_all_books(self):
        print("---- All Books ----")
        self.__library_management_system.display_all_books()

    def run_user_operations(self):
        while True:
            self.display_user_operations_menu()
            choice = input("Enter your choice (1-3): ")
            if choice == "1":
                self.add_new_user()
            elif choice == "2":
                self.view_user_details()
            elif choice == "3":
                self.display_all_users()
            else:
                print("Invalid choice. Please try again.")

    def add_new_user(self):
        print("---- Add a New User ----")
        name = input("Enter the name: ")
        library_id = input("Enter the library ID: ")

        user = User(name, library_id)
        self.__library_management_system.add_user(user)

    def view_user_details(self):
        print("---- View User Details ----")
        user_name = input("Enter the user name: ")

        self.__library_management_system.view_user_details(user_name)

    def display_all_users(self):
        print("---- All Users ----")
        self.__library_management_system.display_all_users()

    def run_author_operations(self):
        while True:
            self.display_author_operations_menu()
            choice = input("Enter your choice (1-3): ")
            if choice == "1":
                self.add_new_author()
            elif choice == "2":
                self.view_author_details()
            elif choice == "3":
                self.display_all_authors()
            else:
                print("Invalid choice. Please try again.")

    def add_new_author(self):
        print("---- Add a New Author ----")
        name = input("Enter the name: ")
        biography = input("Enter the biography: ")

        author = Author(name, biography)
        self.__library_management_system.add_author(author)

    def view_author_details(self):
        print("---- View Author Details ----")
        author_name = input("Enter the author name: ")

        self.__library_management_system.view_author_details(author_name)

    def display_all_authors(self):
        print("---- All Authors ----")
        self.__library_management_system.display_all_authors()


cli = LibraryManagementSystemCLI()
cli.run()

#================================================================================================
#=================================== End of Code=================================================
#================================================================================================


# Author: Roger Block