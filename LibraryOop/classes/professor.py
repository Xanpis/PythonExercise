

class Professor():
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
        return 