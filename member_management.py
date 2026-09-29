"""Functions for registering library members."""

from data import members


def add_member():
    member_id = input("Enter Member ID: ").strip()
    if not member_id:
        print("Error: Member ID cannot be empty.")
    elif member_id in members:
        print("Error: Member ID already exists.")
    else:
        name = input("Enter Member Name: ").strip()
        if not name:
            print("Error: Member name cannot be empty.")
            return
        members[member_id] = {"name": name, "borrowed_books": []}
        print(f"Member '{name}' registered successfully!")
