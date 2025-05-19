    # # Add book in book list of the student max 1 book
    # def add_books(self, book: Book) -> bool:
    #     # validate if is stance of book
    #     self._is_stance_book(book)
    #     # validate book to add in list of sudante
    #     self._validate_book_to_add_student(
    #         book,self._books, self.name
    #     )

    #     # Add book to list
    #     self._books.append(book)
    #     book.status = False
    #     return True

    # def remove_book(self, position: int) -> bool:
    #     # Validate book to remove
    #     self._validate_to_remove(
    #         position, self._books
    #     )

    #     # Remove book
    #     self._books[position].status = True
    #     self._books.pop(position)
    #     return True

    # def show_books(self):
    #     return 


p = input('velue = ').lower()

if not p.isalpha():
    print(p)