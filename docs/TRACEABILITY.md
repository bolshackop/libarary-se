# Traceability Matrix – Library Book Management System

This traceability matrix links user stories to their corresponding sprint, source code functions, unit tests, and Git release tags. It ensures that all requirements are implemented, tested, and released systematically across sprints.

| User Story | Sprint   | Feature Implemented          | Code Location / Function | Test Case Name                     | Release Tag |
|------------|----------|------------------------------|--------------------------|------------------------------------|-------------|
| US-1       | Sprint-1 | Book Registration             | add_book()               | test_add_book_success              | v0.1        |
| US-1       | Sprint-1 | Duplicate Book ID Validation  | add_book()               | test_add_duplicate_book            | v0.1        |
| US-2       | Sprint-2 | Borrow Book                   | borrow_book()            | test_borrow_book                   | v0.2        |
| US-2       | Sprint-2 | Prevent Double Borrow         | borrow_book()            | test_borrow_unavailable_book       | v0.2        |
| US-2       | Sprint-2 | Return Book                   | return_book()            | test_return_book                   | v0.2        |
| US-3       | Sprint-3 | Library Status Report         | generate_report()        | test_report_generation             | v0.3        |

