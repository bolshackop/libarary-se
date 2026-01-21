import unittest
from src.library import Book, Library

class TestLibrary(unittest.TestCase):

    def test_add_book_success(self):
        lib = Library()
        lib.add_book(Book(1, "DSA", "Anuj"))
        self.assertEqual(len(lib.get_all_books()), 1)

    def test_duplicate_book(self):
        lib = Library()
        lib.add_book(Book(1, "DSA", "Anuj"))
        with self.assertRaises(ValueError):
            lib.add_book(Book(1, "OS", "Someone"))

    def test_borrow_available_book(self):
        lib = Library()
        lib.add_book(Book(1, "DSA", "Anuj"))
        lib.borrow_book(1)
        self.assertTrue(lib.books[1].is_borrowed)

    def test_borrow_unavailable_book(self):
        lib = Library()
        lib.add_book(Book(1, "DSA", "Anuj"))
        lib.borrow_book(1)
        with self.assertRaises(ValueError):
            lib.borrow_book(1)

    def test_return_book(self):
        lib = Library()
        lib.add_book(Book(1, "DSA", "Anuj"))
        lib.borrow_book(1)
        lib.return_book(1)
        self.assertFalse(lib.books[1].is_borrowed)

    def test_report_contains_header(self):
        lib = Library()
        report = lib.generate_report()
        self.assertIn("ID | Title | Author | Status", report)

    def test_report_contains_book_entry(self):
        lib = Library()
        lib.add_book(Book(1, "DSA", "Anuj"))
        report = lib.generate_report()
        self.assertIn("1 | DSA | Anuj", report)

if __name__ == "__main__":
    unittest.main()

