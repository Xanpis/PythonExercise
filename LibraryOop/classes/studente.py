from LibraryOop.classes.book import Book
from LibraryOop.interfaces.user import User

class Student(User):
    def __init__(self, name: str, age: int, books=None):
        super().__init__(name, age, books)

    def show_books(self) -> list:
        return self._books
    
    def add_books(self, book: Book) -> bool:
        return True
