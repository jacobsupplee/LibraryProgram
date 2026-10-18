# Python Library Catalog

This is a small Python command-line program for keeping track of books in a library. You can view which books are available, borrow a book, and return it. The program uses a menu to let you choose what to do and checks for invalid selections.

## Features

- View available and borrowed books
- Borrow a book from the available list
- Return a borrowed book
- Validate menu choices and book selections
- Handle invalid input and empty lists

## Built with

- Python 3
- Lists and collection operations
- Functions and control flow
- Exception handling
- Command-line menus

## Running it

Make sure Python 3 is installed, then run this from the project directory:

```bash
python LibraryProgram.py
```

No extra packages are required.

## Notes

The program keeps track of books using in-memory lists, so the changes are lost when you close it. It doesn't have a database, user accounts, or due-date tracking yet.

This project gave me practice with Python functions, managing collections, validating user input, and building a menu-driven program. Saving the inventory between runs would be a good next step.
