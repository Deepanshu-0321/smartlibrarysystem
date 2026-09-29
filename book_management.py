"""Functions for adding books."""

from data import books


def add_book():
    book_id = input("Enter Book ID: ").strip()
    if not book_id:
        print("Error: Book ID cannot be empty.")
    elif book_id in books:
        print("Error: Book ID already exists.")
    else:
        title = input("Enter Book Title: ").strip()
        author = input("Enter Author: ").strip()
        if not title or not author:
            print("Error: Book title and author cannot be empty.")
            return
        books[book_id] = {
            "title": title,
            "author": author,
            "status": "Available",
            "issued_to": None,
        }
        print(f"Book '{title}' added successfully!")
