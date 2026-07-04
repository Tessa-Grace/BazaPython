class Book:
    """Класс, в котором передается название и автор книги"""
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    
class Library:
    """Класс хранит список книг и имеет методы add_book, list_books"""
    def __init__(self):
        self.ls = []

    def add_book(self, book):
        self.ls.append(book)

    def list_books(self):
        return self.ls

library = Library()
library.add_book(Book('1984', 'George Orwell'))
library.add_book(Book('Dune', 'Frank Herbert'))

books = library.list_books()
for book in books:
    print(f'{book.author} - {book.title}')
