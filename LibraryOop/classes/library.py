

class Library():


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
