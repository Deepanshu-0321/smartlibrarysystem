# Smart Library Management System (Flat Script without OOP or functions/def)

# Initial Data of books
books = {
    "101": {"title": "Python Programming", "author": "John Doe", "status": "Available", "issued_to": None},
    "102": {"title": "Data Structures", "author": "Jane Smith", "status": "Available", "issued_to": None},
    "103": {"title": "java programming", "author": "ken narnold","status": "Available","issued_to": None},
    "104": {"title": "C++", "author": "Bjarne Stroustrup","status": "Available","issued_to": None}
}
# initil data of members
members = {
    "M01": {"name": "Alice", "borrowed_books": []},
    "M02": {"name": "Bob", "borrowed_books": []},
    "M03": {"name": "john", "borrowed_books": []},
    "M04": {"name": "max",  "borrowed_books": []}
}
# we use while loop in which the condition is always true that's why it run always
while True:
    print("\n=== SMART LIBRARY SYSTEM ===")
    print("1. Add Book")
    print("2. Add Member")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Display All Books")
    print("7. Display All Members")
    print("8. Exit")

# Read option input and strip extra spaces to avoid unintended input errors    
    choice = input("Select an option (1-8): ").strip()
    # Add new books
    if choice == "1":
        book_id = input("Enter Book ID: ").strip()
        if book_id in books:
            print("Error: Book ID already exists.")
        else:
            title = input("Enter Book Title: ").strip()
            author = input("Enter Author: ").strip()

           # Store initial record directly into master books dictionary 
            books[book_id] = {
                "title": title,
                "author": author,
                "status": "Available",
                "issued_to": None
            }
            print(f"Book '{title}' added successfully!")
    # Register new member     
    elif choice == "2":
        member_id = input("Enter Member ID: ").strip()
        # verify member id uniqueness
        if member_id in members:
            print("Error: Member ID already exists.")
        else:
            name = input("Enter Member Name: ").strip()
            members[member_id] = {
                "name": name,
                "borrowed_books": []
            }
            print(f"Member '{name}' registered successfully!")
    # search books        
    elif choice == "3":
        query = input("Enter Book Title or Author to search: ").strip().lower()
        found = False
        print("\n" + "="*60)
        print(f"{'ID':<10} {'Title':<25} {'Author':<15} {'Status':<10}")
        print("="*60)

        # Linear iteration through dictionary key-value pairs for string matching
        for b_id, details in books.items():
            if query in details["title"].lower() or query in details["author"].lower():
                print(f"{b_id:<10} {details['title']:<25} {details['author']:<15} {details['status']:<10}")
                found = True
        print("="*60)
        if not found:
            print("No matching books found.")
    # issue book to member        
    elif choice == "4":
        book_id = input("Enter Book ID to issue: ").strip()
        #Validate book existence
        if book_id not in books:
            print("Error: Book not found.")
        #Ensure book isn't already borrowed
        elif books[book_id]["status"] == "Issued":
            print(f"Error: Book is already issued to Member ID '{books[book_id]['issued_to']}'.")
        else:
            member_id = input("Enter Member ID: ").strip()
            if member_id not in members:
                print("Error: Member not registered.")
            # Update relation: Mark book as Issued and append Book ID to member's array    
            else:
                books[book_id]["status"] = "Issued"
                books[book_id]["issued_to"] = member_id
                members[member_id]["borrowed_books"].append(book_id)
                print(f"Book '{books[book_id]['title']}' successfully issued to {members[member_id]['name']}.")
                
    elif choice == "5":
        book_id = input("Enter Book ID to return: ").strip()
        if book_id not in books:
            print("Error: Book not found.")
        elif books[book_id]["status"] == "Available":
            print("Error: This book is not currently issued.")
        else:
            member_id = books[book_id]["issued_to"]
            books[book_id]["status"] = "Available"
            books[book_id]["issued_to"] = None
            if member_id in members and book_id in members[member_id]["borrowed_books"]:
                members[member_id]["borrowed_books"].remove(book_id)
            print(f"Book '{books[book_id]['title']}' successfully returned.")
            
    elif choice == "6":
        if not books:
            print("No books available in the library.")
        else:
            print("\n" + "="*60)
            print(f"{'ID':<10} {'Title':<25} {'Author':<15} {'Status':<10}")
            print("="*60)
            for b_id, details in books.items():
                print(f"{b_id:<10} {details['title']:<25} {details['author']:<15} {details['status']:<10}")
            print("="*60)
            
    elif choice == "7":
        if not members:
            print("No registered members.")
        else:
            print("\n" + "="*50)
            print(f"{'Member ID':<12} {'Name':<20} {'Borrowed Books':<15}")
            print("="*50)
            for m_id, details in members.items():
                borrowed = ", ".join(details["borrowed_books"]) if details["borrowed_books"] else "None"
                print(f"{m_id:<12} {details['name']:<20} {borrowed:<15}")
            print("="*50)
#terminating the programm            
    elif choice == "8":
        print("Exiting system. Goodbye!")
        break
# unknown input handler        
    else:
        print("Invalid selection. Please choose a number between 1 and 8.")