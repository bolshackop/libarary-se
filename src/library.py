class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book_id, title, author):
        if book_id in self.books:
            raise ValueError("Duplicate Book ID")
        self.books[book_id] = {
            "title": title,
            "author": author,
            "borrowed": False
        }

    def borrow_book(self, book_id):
        if book_id not in self.books:
            raise ValueError("Book not found")
        if self.books[book_id]["borrowed"]:
            raise ValueError("Book already borrowed")
        self.books[book_id]["borrowed"] = True

    def return_book(self, book_id):
        if book_id not in self.books:
            raise ValueError("Book not found")
        self.books[book_id]["borrowed"] = False

    def generate_report(self):
        report = "Book ID | Title | Author | Status\n"
        for book_id, data in self.books.items():
            status = "Borrowed" if data["borrowed"] else "Available"
            report += f"{book_id} | {data['title']} | {data['author']} | {status}\n"
        return report

