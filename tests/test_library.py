import unittest
from src.library import Library


class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.library = Library()

    def test_add_book_success(self):
        self.library.add_book(1, "Clean Code", "Robert C. Martin")
        self.assertIn(1, self.library.books)

    def test_add_duplicate_book_id(self):
        self.library.add_book(1, "Clean Code", "Robert C. Martin")
        with self.assertRaises(ValueError):
            self.library.add_book(1, "Refactoring", "Martin Fowler")

    def test_borrow_book_success(self):
        self.library.add_book(1, "Clean Code", "Robert C. Martin")
        self.library.borrow_book(1)
        self.assertTrue(self.library.books[1]["borrowed"])

    def test_borrow_nonexistent_book(self):
        with self.assertRaises(ValueError):
            self.library.borrow_book(99)

    def test_borrow_already_borrowed_book(self):
        self.library.add_book(1, "Clean Code", "Robert C. Martin")
        self.library.borrow_book(1)
        with self.assertRaises(ValueError):
            self.library.borrow_book(1)

    def test_return_book(self):
        self.library.add_book(1, "Clean Code", "Robert C. Martin")
        self.library.borrow_book(1)
        self.library.return_book(1)
        self.assertFalse(self.library.books[1]["borrowed"])

    def test_generate_report(self):
        self.library.add_book(1, "Clean Code", "Robert C. Martin")
        report = self.library.generate_report()
        self.assertIn("Clean Code", report)
        self.assertIn("Available", report)


if __name__ == "__main__":
    unittest.main()

