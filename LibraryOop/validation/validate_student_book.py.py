

class ValidateStudantBook:
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
            return False

        # validate if the estudante can take the book
        if len(book_list) < 0 or len(book_list) >= 1:
            return False
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
