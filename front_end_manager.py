from library_admin import LibraryAdmin
from valid_input import input_valid_int

class FrontendManager:
    def __init__(self):
        self.library_admin = LibraryAdmin()

    
    def print_menu(self):
        print('\nProgram Options:')
        messages = [
            'Add book',
            'Print Library books',
            'Search books by prefix',
            'Add user',
            'Borrow book',
            'Return book',
            'Print users borrowed a book',
            'Print all users',
            'End the program'
        ]
        # let's add the order 1 2 3 4...
        messages = [f'{idx+1}) {msg}' for idx, msg in enumerate(messages)]
        print('\n'.join(messages))
        msg = f'Enter your choice (from 1 to {len(messages)}): '
        return input_valid_int(msg, 1, len(messages))
    

    def run(self):
        while True:
            choice = self.print_menu()

            ## adding a book to the library
            if choice == 1:
                book_name = input("Enter book name: ")
                book_quantity = input_valid_int("Enter quantity of the book: ", 1, 1000000)
                if not self.library_admin.book_added_before(book_name):
                    self.library_admin.add_book(book_name, book_quantity)
                else:
                    print("Sorry! This book is added before")
            
            ## print all library books
            elif choice == 2:
                print(self.library_admin.books_list())

            ## Search by book prefix
            elif choice == 3:
                book_prefix_name = input("Enter book prefix or name: ")
                search = self.library_admin.search_by_prefix(book_prefix_name)
                for book in search:
                    print(book)

            ## add user
            elif choice == 4:
                user_name = input("Enter user name: ")
                if not self.library_admin.user_added_before(user_name):
                    self.library_admin.add_user(user_name)
                else:
                    print("Sorry! This user is added before")
            
            ## borrow book
            elif choice == 5:
                user_name = input("Enter user name: ")
                book_name = input("Enter book name: ")
                
                if self.library_admin.allowed_borrow_book(user_name, book_name):
                    user_flag, book_flag, _, _ = self.library_admin.allowed_borrow_book(user_name, book_name)

                    if user_flag and book_flag:
                        self.library_admin.borrow_book(user_name, book_name)
                        print("Done!")
                    elif not user_flag and book_flag:
                        print("this user borrowed this book before")
                    elif user_flag and not book_flag:
                        print("This book is out of stock")
                    else:
                        print("this user borrowed this book before")
                        print("This book is out of stock")
                else:
                    print("Please check your username or bookname")

            ## Return book
            elif choice == 6:
                user_name = input("Enter user name: ")
                book_name = input("Enter book name: ")

                if self.library_admin.allowed_return_book(user_name, book_name):
                    user_flag, book_flag, _, _ = self.library_admin.allowed_return_book(user_name, book_name)

                    if user_flag and book_flag:
                        self.library_admin.return_book(user_name, book_name)
                        print("Done!")
                    elif not user_flag and book_flag:
                        print("this user didn't borrow this book")
                else:
                    print("Please check your username or bookname")

            ## Print users borrowed a book
            elif choice == 7:
                book_name = input("Enter book name: ")
                users = self.library_admin.users_borrowed_a_book(book_name)
                if users==set():
                    print("There is no one borrowed this book")
                elif users is None:
                    print("Please check your bookname")
                else:
                    print("List of users borrowed this book:")
                    for user in users:
                        print(user)
                
                        
                

            ## Print all users
            elif choice == 8:
                all_users = self.library_admin.user_books
                for user, books in all_users.items():
                    if books == set():
                        print(user)
                    else:
                        print(user)
                        print("Borrowed books:")
                        for book in books:
                            print(book)
                    print()

            elif choice == 9:
                break

if __name__ == "__main__":
    app = FrontendManager()
    app.run()

