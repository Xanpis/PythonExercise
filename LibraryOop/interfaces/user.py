
from abc import ABC, abstractmethod
from classes.book import Book

class User(ABC):
    def __init__(self, name: str, age: int, books=None):
        self.name = name
        self.age = age
        self.id = 0
        self.books = []

    # shows the books taken by the user
    @abstractmethod
    def show_books(self) -> list:...

    # Add book to list
    @abstractmethod
    def add_books(self, book:Book) -> bool: ...

    # Remove books taken by the user
    @abstractmethod
    def remove_book(self, position: int) -> bool: ...
