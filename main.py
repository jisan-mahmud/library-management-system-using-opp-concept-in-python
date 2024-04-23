class Book:
    def __init__(self, name, author, id) -> None:
        self.name = name
        self.author = author
        self.id = id
    def __str__(self) -> str:
        return f'Name: {self.name}, author: {self.author}, id: {self.id}'

class User:
    def __init__(self,name: str, age: int, user_id: int) -> None:
        self.name = name
        self.age = age
        self.user_id = user_id
        self.limit = 0
        self.borrow_books = []

    def borrow_book(self, book_id):
        for book in self.borrow_books:
            if book.id == id:
                print('Your are already borrow this book!')
            else:
                if self.limit > 0:
                    self.borrow_books.append(book)
                    print('Succesfully borrow this book!')
                    self.limit -= 1
                else:
                    print('borrow limit reached.')

    def __str__(self) -> str:
        return f'Name: {self.name}, age: {self.age}, user_id: {self.user_id}'

    def return_book(self, book_id):
        for book in self.borrow_books:
            if book_id == book.id:
                self.borrow_books.remove(book)
                self.limit += 1

class Library:
    def __init__(self, name: str, limit: int) -> None:
        self.name = name
        self.limit = limit
        self.books = []
        self.user = []
        self.borrow_books = []

    def add_book(self, book, total_copy):
        for book_info in self.books:
            if book_info.get('book') == book:
                book_info['total_copy'] += total_copy
                return
        self.books.append({"book": book, "total_copy": total_copy})

    def display_book(self):
        for book_info in self.books:
            print(f'{book_info.get('book')},', f'Total Copy: {book_info.get('total_copy')}')

    def add_user(self, user):
        if user in self.user:
            print('This user already exits in libary.')
        else:
            self.user.append(user)
            user.limit = self.limit
            print('Congratulations registration succesfull!')

    def borrow_book(self, book_id, user_id):
        for user in self.user:
            print(user)
            if user.user_id == user_id:
                for book_info in self.books:
                    if book_info.get('book').id == book_id:
                        if {'book': book, 'user': user} in self.borrow_books:
                            print('You have already borrow this book.')
                        else:
                            user.borrow_book(book)
                            self.borrow_books.append({'book': book, 'user': user})
                    else:
                        print('Book not exits!')
            else:
                print('This user is not registered user.\n')
    def return_book(self, book_id, user_id):
        for user in self.user:
            if user_id == user.user_id:
                for book_info in self.borrow_books:
                    if book_info.get('book').id == book_id:
                        print('Return Succesfully!')
                        user.return_book(book_id)
                        self.borrow_books.remove(book_info)
                    else:
                        print('You have no borrow in this libary for this book.')
            else:
                print('User Not Found')

    def display_borrow(self):
        for book_info in self.borrow_books:
            print(book_info.get('book'))

library = Library('Knowledge House', 10)
book = Book('Web devepolemnt', 'HM Nayem', 101)
library.add_book(book, 10)
while True:
    print('1. Add a book to the library')
    print('2. Show all books')
    print('3. Register a user')
    print('4. Borrow a book')
    print('5. Return a book')
    print('6. Display all borrow book')
    print('0. Exit')

    user_choice = input('Choose one option: ')

    if user_choice == '0':
        break
    elif user_choice == '1':
        book_name = input('Enter a book name: ')
        author = input('Enter author name: ')
        total_copy = int(input('Enter total copies: '))
        book = Book(book_name, author)
        library.add_book(book, total_copy)
    elif user_choice == '2':
        print('Available book: ')
        print('---------------------------')
        library.display_book()
        print('\n')
    elif user_choice == '3':
        name = input('Enter your name: ')
        age = input('Enter your age: ')
        user_id = int(input('Enter your user id: '))
        user = User(name, age, user_id)
        library.add_user(user)
    elif user_choice == '4':
        book_id = int(input('Enter book id: '))
        user_id = int(input('Enter user_id: '))
        library.borrow_book(book_id, user_id)
    elif user_choice == '5':
        book_id = int(input('Enter book id: '))
        user_id = int(input('Enter user_id: '))
        library.return_book(book_id, user_id)
    elif user_choice == '6':
        library.display_borrow()
    else:
        print('Type a valid option...')