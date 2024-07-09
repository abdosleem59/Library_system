from book import Book
from user import User
import rnd
class LibraryAdmin:
    def __init__(self):
        self.existing_ids = set()
        self.book_users = {}
        self.user_books = {}
        self.prefix_search ={}

    def book_added_before(self, name):
        for book, value in self.book_users.items():
            if book.name == name:
                return book, value
        return False


    def add_book(self,name,quantity):
        id = rnd.generate_unique_numeric_user_id(self.existing_ids)
        book = Book(id, name, quantity)
        self.book_users[book] = set()
        self.add_prefixes_for_book(book)


    def add_prefixes_for_book(self, book):
        ## adding all possible prefixes for the book name
        for idx, _ in enumerate(book.name):
            pre = book.name[:idx+1]
            self.prefix_search.setdefault(pre,[])
            self.prefix_search[pre].append(book)

    
    def search_by_prefix(self, book_prefix_name):
        return self.prefix_search[book_prefix_name]


    def books_list(self):
        for book in self.book_users.keys():
            return book


    def user_added_before(self,name):
        for user in self.user_books.keys():
            if user.name == name:
                return user
        return False
    

    def add_user(self,name):
        id = rnd.generate_unique_numeric_user_id(self.existing_ids)
        u = User(id, name)
        self.user_books[u] = set()

    def found_book_and_user(self, user_name, book_name):
        book = False
        if self.book_added_before(book_name):
            book, user_lst = self.book_added_before(book_name)
        
        user = self.user_added_before(user_name) 
        if book and user:
            return user, book, user_lst
        else:
            return None


    def allowed_borrow_book(self, user_name, book_name):
        user_flag, book_flag = False, False
        if self.found_book_and_user(user_name, book_name) is not None:
            user, book, user_lst= self.found_book_and_user(user_name, book_name)
            if book.quantity > 0:
                    book_flag = True
            if user not in user_lst:
                    user_flag = True
            return user_flag, book_flag, user, book
        return False


    def borrow_book(self, user_name, book_name):
        _, _, user, book = self.allowed_borrow_book(user_name, book_name)
        self.user_books[user].add(book)
        self.book_users[book].add(user)
        book.borrowed+=1
        book.quantity-=1
        

    def allowed_return_book(self,user_name, book_name):
        user_flag, book_flag = False, True
        if self.found_book_and_user(user_name, book_name) is not None:
            user, book, user_lst= self.found_book_and_user(user_name, book_name)
            if user in user_lst:
                    user_flag = True
            return user_flag, book_flag, user, book
        return False


    def return_book(self,user_name, book_name):
        _,_, user, book=self.allowed_return_book(user_name, book_name)
        self.user_books[user].remove(book)
        self.book_users[book].remove(user)
        book.borrowed-=1
        book.quantity+=1
    

    def users_borrowed_a_book(self, book_name):
        for book, value in self.book_users.items():
            if book.name == book_name:
                return value
        return None
