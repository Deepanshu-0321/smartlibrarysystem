# Smart Library Management System

## Problem Statement
Managing books and library members manually can take time and make it difficult to track which books are available or issued. This project provides a simple menu-based system to help keep basic library records and manage book issue and return activities.

## Scope of the Project
The project covers basic library tasks through a Python command-line interface. A user can add books, register members, search for books, issue books to registered members, return issued books, and display the current book and member records.

The program stores its records in Python dictionaries while it is running. The data is not saved to a file or database, so the records return to their initial values when the program is closed and started again. The project is intended for basic demonstration and learning purposes rather than managing a large library.

## Target Users
- Students learning Python programming and basic data handling.
- Small libraries or classroom projects that need a simple demonstration of book records.
- A library operator who wants to try basic book issue and return workflows.

## High-Level Features
- **Add Book:** Enter a book ID, title, and author to add a book to the current records.
- **Add Member:** Register a member using a member ID and name.
- **Search Book:** Search for books by title or author.
- **Issue Book:** Issue an available book to a registered member.
- **Return Book:** Mark an issued book as available again and update the member's borrowed-book list.
- **Display All Books:** View book IDs, titles, authors, and availability status.
- **Display All Members:** View member IDs, names, and borrowed book IDs.
- **Input Checks:** Check for duplicate IDs, missing books or members, and attempts to issue or return books in invalid states.
