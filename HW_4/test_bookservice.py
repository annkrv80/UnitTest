import unittest
from unittest.mock import patch

from book_service import BookService


class TestBookService(unittest.TestCase):
    @patch('book_service.BookRepository')
    def test_get_info_book(self, mock_book):
        book_id = 5
        self.service = BookService(mock_book)
        self.service.book_service(book_id)
        self.service.book_repository.get_info_book.assert_called_once_with(book_id)
