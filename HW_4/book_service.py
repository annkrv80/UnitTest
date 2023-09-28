class BookRepository:
    def get_info_book(self, book_id: int):
        return f'Информация о книги {book_id}'


class BookService:
    def __init__(self, book_repository: BookRepository):
        self._book_repository = book_repository

    @property
    def book_repository(self):
        return self._book_repository

    def book_service(self, book_id: int) -> str:
        book_info = self._book_repository.get_info_book(book_id)
        return book_info
