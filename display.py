"""Functions for displaying library books and members."""

from data import books, members


def display_books():
    if not books:
        print("No books available in the library.")
        return

    print("\\n" + "=" * 70)
    print(f"{'ID':<10} {'Title':<30} {'Author':<20} {'Status':<10}")
    print("=" * 70)
    for book_id, details in books.items():
        print(f"{book_id:<10} {details['title']:<30} {details['author']:<20} {details['status']:<10}")
    print("=" * 70)


def display_members():
    if not members:
        print("No registered members.")
        return

    print("\\n" + "=" * 60)
    print(f"{'Member ID':<12} {'Name':<20} {'Borrowed Books':<25}")
    print("=" * 60)
    for member_id, details in members.items():
        borrowed = ", ".join(details["borrowed_books"]) if details["borrowed_books"] else "None"
        print(f"{member_id:<12} {details['name']:<20} {borrowed:<25}")
    print("=" * 60)
