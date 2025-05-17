
from class_book import Book
from abc import ABC, abstractmethod



class People(ABC):
    def __init__(self, name: str, age: int, books=None):
        self.name = name
        self.ege = age
        self._books = []

    # shows the books taken by the user
    @abstractmethod
    def show_books(self) -> list:
        if not self._books:
            raise TypeError(f" '{self.name}' you don't have any books to list")
        return self._books

    # Add book to list
    @abstractmethod
    def add_books(self, book:Book) -> bool: ...

    # Remove books taken by the user
    @abstractmethod
    def remove_book(self, position: int) -> bool: ...


class Book_Validation:
    # Validate position of the book to remove.
    def _validate_to_remove(
            self, position: int, book_list: list
        ) -> bool:
        # Size of list
        list_size = len(book_list)
        # if the position is in list
        is_in_list = True if position >= 0 and \
            position < list_size else False

        # Finding book to remove
        if not book_list or not is_in_list:
            raise TypeError("The book cannot be found for remove.")
        return True

    # validate if is stance of book
    def _is_stance_book(self, book: Book) -> bool:
        if not isinstance(book, Book):
            raise TypeError('The value is not a instance of book')
        return True

    # Validate book to add
    def _validate_book_to_add_student(
            self, book: Book, book_list:list,  name:str
        ) -> bool:
        # validate if the book the is already in use
        if book.status == False:
            raise TypeError(
                f'Hello "{name}" you cannot take the book in use'
            )

        # validate if the estudante can take the book
        if len(book_list) < 0 or len(book_list) >= 1:
            raise TypeError(
                f'Hello "{name}" you only can take 1 book'
            )
        return True

    # Validate book to add
    def _validate_book_to_add_professor(
            self, book: Book, book_list:list,  name:str
        ) -> bool:
        # validate if the book the is already in use
        if book.status == False:
            raise TypeError(
                f'Hello "{name}" you cannot take the book in use'
            )

        # validate if the professor can take the book
        if len(book_list) < 0 or len(book_list) >= 3:
            raise TypeError(
                f'Hello "{name}" you only can take 3 books'
            )
        return True

    def __repr__(self):
        return f"{self.__dict__}"


class Student(Book_Validation, People):
    # Add book in book list of the student max 1 book
    def add_books(self, book: Book) -> bool:
        # validate if is stance of book
        self._is_stance_book(book)
        # validate book to add in list of sudante
        self._validate_book_to_add_student(
            book,self._books, self.name
        )

        # Add book to list
        self._books.append(book)
        book.status = False
        return True

    def remove_book(self, position: int) -> bool:
        # Validate book to remove
        self._validate_to_remove(
            position, self._books
        )

        # Remove book
        self._books[position].status = True
        self._books.pop(position)
        return True

    def show_books(self):
        return super().show_books()


class Professor(Book_Validation, People):
    # Add book in book list of the professor max 3 book
    def add_books(self, book: Book) -> bool:
        # validate if is stance of book
        
        self._is_stance_book(book)
        # Validate book to add in list of professor
        self._validate_book_to_add_professor(
            book,self._books, self.name
        )

        # Add book to list
        self._books.append(book)
        book.status = False
        return True

    def remove_book(self, position: int) -> bool:
        # Validate book to remove
        self._validate_to_remove(
            position, self._books
        )

        # Remove book
        self._books[position].status = True
        self._books.pop(position)
        return True

    def show_books(self):
        return super().show_books()


bo = 'a'
if __name__ == '__main__':
    try:
        b1 = Book('jão pé de feijão ', 'Ciência')
        b2 = Book('jão pé de feijão ', 'Ciência')
        b3 = Book('jão pé de feijão ', 'Ciência')
        b4 = Book('jão pé de feijão ', 'Ciência')

        # a = Student('Maria', 34)
        # a.add_books(b1)
        # # a.add_books(b1)
        # a.remove_book(0)
        
        # # a.add_books(b2)

        # print(b1)
        # print(a)

        p = Professor('Jonas', 50)
        # p.add_books(b3)
        p.add_books(b1)
        p.add_books(b2)
        p.add_books(b3)
        
        print(p)

    except TypeError as ex:
        print(ex)
