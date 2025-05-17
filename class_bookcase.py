from sqlalchemy import values
from class_user import Student
from class_book import Book


class Book_shelf_validate:
    # if book is a instance of book
    def _is_stance_book(self, book: Book) -> bool:
        if not isinstance(book, Book):
            raise TypeError('The value is not a instance of book')
        return True

    # Validate genre and book is the genre for add
    def _validate_to_add_book_in_shelf(
        self, genre: str, book: Book, dic_bookshelf: dict
    ):
        # Validate if genre is already on the shelf
        if not genre in dic_bookshelf.keys():
            raise TypeError(
                f'The genre "{genre}" could not be identified.'
            )

        # Validate if the genre are the same
        if not book.genre == genre:
            raise TypeError(
                f'the genre "{genre}" of the book is not the same as the one on the shelf.'
            )

        #
        for books_value_list in dic_bookshelf.values():
            for books_value in books_value_list:
                if book.name == books_value.name:
                    raise TypeError('This book is already on the shelf')
        return True

    def validate_to_add_shelf(
            self, genre: str, dic_bookshelf: dict
        ) -> bool:
        if genre in dic_bookshelf.keys():
            raise TypeError(f'The genre "{genre}" is already on the shelf')
        return True

    def validate_to_remove_shelf(
            self, genre: str, dic_bookshelf: dict
        ) -> bool:
        if genre not in dic_bookshelf.keys():
            raise TypeError(f'The genre " {genre} " cannot be removed')
        return True


class Bookcase(Book_shelf_validate):
    def __init__(self):
        self.dic_bookshelf = {
            'Physics': [],
            'Science': [],
            'Technology': [],
            'Philosophy': [],
        }

    # Add book on the shelf
    def add_book_in_shelf(self, genre: str, book: Book) -> bool:
        # validate if is book instance
        self._is_stance_book(book)
        # Validate genre of the book to add
        self._validate_to_add_book_in_shelf(
            genre, book, self.dic_bookshelf
        )

        # Add book on the shelf
        self.dic_bookshelf[genre].append(book)
        return True
    
    def remove_book_in_shelf(self, genre, dic_bookshelf):
        if genre not in dic_bookshelf:
            raise TabError('')

    # Put the gente and empty shelf
    def add_shelf(self, genre: str) -> bool:
        # validate if the already have the shelf
        self.validate_to_add_shelf(
            genre, self.dic_bookshelf
        )

        self.dic_bookshelf.update({genre: []})
        return True

    # Remove the shelf and the books into
    def remove_shelf(self, genre: str) -> bool:
        # Validate if have the shelf
        self.validate_to_remove_shelf(genre, self.dic_bookshelf)
        del self.dic_bookshelf[genre]
        return True

    def show_bookshelf(self) -> dict:
        if not self.dic_bookshelf:
            raise TypeError('Shelf is empty')
        return self.dic_bookshelf


if __name__ == "__main__":
    try:
        s = Student('Maria', 45)
        b1 = Book('a', 'Physics')
        b2 = Book('b', 'Physics')
        b3 = Book('c', 'Physics')
        b4 = Book('d', 'Philosophy')

        b = Bookcase()
        # b.add_book_in_shelf('Physics', b1
        b.add_book_in_shelf('Physics', b1)
        b.add_book_in_shelf('Physics', b2)
        b.add_book_in_shelf('Physics', b3)
        b.add_book_in_shelf('Philosophy', b4)
        # b.add_book_in_shelf('Physics', b4)

        for i, j in b.dic_bookshelf.items():
            print(i, len(j))
            for p in j:
                print('  ', p.name, p.genre)
            print()

    except TypeError as ex:
        print(ex)
