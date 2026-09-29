"""Search books by title or author."""

from data import books


def search_book():
    query = input("Enter Book Title or Author to search: ").strip().lower()
    if not query:
        print("Please enter a title or author to search.")
        return

    print("\\n" + "=" * 70)
    print(f"{'ID':<10} {'Title':<30} {'Author':<20} {'Status':<10}")
    print("=" * 70)
    found = False
    for book_id, details in books.items():
        if query in details["title"].lower() or query in details["author"].lower():
            print(f"{book_id:<10} {details['title']:<30} {details['author']:<20} {details['status']:<10}")
            found = True
    print("=" * 70)
    if not found:
        print("No matching books found.")
