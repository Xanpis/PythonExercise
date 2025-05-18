
from abc import ABC, abstractmethod
from LibraryOop.classes.book import Book

class User(ABC):
    def __init__(self, name: str, age: int, books=None):
        self.name = name
        self.ege = age
        self._books = []

    # shows the books taken by the user
    @abstractmethod
    def show_books(self) -> list:...

    # Add book to list
    @abstractmethod
    def add_books(self, book:Book) -> bool: ...

    # Remove books taken by the user
    @abstractmethod
    def remove_book(self, position: int) -> bool: ...
