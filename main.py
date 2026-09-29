"""Main menu for the Smart Library Management System."""

from book_management import add_book
from member_management import add_member
from search_books import search_book
from circulation import issue_book, return_book
from display import display_books, display_members


def main():
    while True:
        print("\\n=== SMART LIBRARY SYSTEM ===")
        print("1. Add Book")
        print("2. Add Member")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Display All Books")
        print("7. Display All Members")
        print("8. Exit")

        choice = input("Select an option (1-8): ").strip()

        if choice == "1":
            add_book()
        elif choice == "2":
            add_member()
        elif choice == "3":
            search_book()
        elif choice == "4":
            issue_book()
        elif choice == "5":
            return_book()
        elif choice == "6":
            display_books()
        elif choice == "7":
            display_members()
        elif choice == "8":
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid selection. Please choose a number between 1 and 8.")


if __name__ == "__main__":
    main()
