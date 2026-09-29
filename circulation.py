"""Functions for issuing and returning books."""

from data import books, members


def issue_book():
    book_id = input("Enter Book ID to issue: ").strip()
    if book_id not in books:
        print("Error: Book not found.")
        return
    if books[book_id]["status"] == "Issued":
        print(f"Error: Book is already issued to Member ID '{books[book_id]['issued_to']}'.")
        return

    member_id = input("Enter Member ID: ").strip()
    if member_id not in members:
        print("Error: Member not registered.")
        return

    books[book_id]["status"] = "Issued"
    books[book_id]["issued_to"] = member_id
    members[member_id]["borrowed_books"].append(book_id)
    print(f"Book '{books[book_id]['title']}' successfully issued to {members[member_id]['name']}.")


def return_book():
    book_id = input("Enter Book ID to return: ").strip()
    if book_id not in books:
        print("Error: Book not found.")
        return
    if books[book_id]["status"] == "Available":
        print("Error: This book is not currently issued.")
        return

    member_id = books[book_id]["issued_to"]
    books[book_id]["status"] = "Available"
    books[book_id]["issued_to"] = None
    if member_id in members and book_id in members[member_id]["borrowed_books"]:
        members[member_id]["borrowed_books"].remove(book_id)
    print(f"Book '{books[book_id]['title']}' successfully returned.")
