
from __future__ import annotations
class Book:
    '''
    This class creates a book object that contains the book title and author.
    The methods of this class take the name and title of the book as a string and create a book object.
    '''
    def __init__(self, title: str, author: str) -> None:
        '''
        Creates an object by taking the title and author.
        '''
        self.title = title
        self.author = author

    def get_title(self):
        return self.title
    
    def set_title(self, title: str):
        self.title = title

    def get_author(self):
        return self.author
    
    def set_author(self, author: str):
        self.author= author


class Library:

    '''
    In this class, you can add books to your list or display a list of books.
    '''
    def __init__(self):
        '''
        This method creates a list of books as a dictionary.
        '''
        self.list_book = []

    def add_book(self, title: str, author: str) -> Book:
        '''
        This method creates a new book by taking the title and author of the book and calling the Book method and adding it to our list.
        '''
        new_book = Book(title = title, author = author)
        self.list_book.append(new_book)

    def list_books(self):
        '''
        This method prints our list of books.
        '''
        for book in self.list_book:
            print(f"{book.get_title()} by {book.get_author()}")


# test_case_1:
# library = Library()  
# library.add_book("1984", "George Orwell")  
# library.add_book("To Kill a Mockingbird", "Harper Lee")  
# library.list_books()