"""

Name: Jacob Supplee
Date: 07/03/2026
Project Title: Library Program
Version: 1.0
Program Description: This program provides an interactive digital library menu in which a user can display the
available books in the library, borrow a book, return a book, and exit the program.

"""

#Initialize book lists
availableBooks = ["To Kill A Mockingbird", "The Hunger Games", "The Maze Runner", "Lord of the Flies", "Dune"]

borrowedBooks = []

#Displays the available and borrowed books in the library
def displayBooks():

    #Output - available books
    print("List of available books: ")

    if len(availableBooks) == 0:
        print("\nNo books available.")
    else:
        for i, book in enumerate(availableBooks, start = 1):
            print(f"{i}. {book}")

    #Output - borrowed books
    print("\nList of borrowed books: ")

    if len(borrowedBooks) == 0:
        print("\nThere are no borrowed books.")
    else:
        for i, book in enumerate(borrowedBooks, start = 1):
            print(f"{i}. {book}")

        print()

#Enables user to borrow a book from the library
def borrowBook():
    if len(availableBooks) == 0:
        print("\nThere are no books available to borrow.")
        return

    #Output - available books
    print("\nBooks available to borrow: ")
    for i, book in enumerate(availableBooks, start = 1):
        print(f"{i}. {book}")

    try:
        #Input
        bookNumber = int(input("\nEnter the number of the book you would like to borrow: "))

        if 1 <= bookNumber <= len(availableBooks):
            #Process
            bookTitle = availableBooks.pop(bookNumber - 1)
            borrowedBooks.append(bookTitle)

            #Output
            print(f"\n{bookTitle} has been borrowed successfully.")
        else:
            print("Invalid book number.")

    except ValueError:
        print("Please enter a valid book number.")

#Function to return a book
def returnBook():
    if len(borrowedBooks) == 0:
        print("\nThere are no borrowed books to return.")
        return

    #Output - borrowed books
    print("\nBorrowed Books: ")
    for i, book in enumerate(borrowedBooks, start = 1):
        print(f"{i}. {book}")

    try:
        #Input
        bookNumber = int(input("\nEnter the book number you would like to return: "))
        if 1 <= bookNumber <= len(borrowedBooks):

            #Process
            bookTitle = borrowedBooks.pop(bookNumber - 1)
            availableBooks.append(bookTitle)

            #Output
            print(f"\n{bookTitle} has been returned.")
        else:
            print("Invalid book number.")

    except ValueError:
        print("Please enter a valid book number.")

#Beginning of main execution

userDecision = 0

while userDecision != 4:
    print("\nWelcome to The Jacob Library Online Catalogue!")
    print("\n1. Display available and borrowed books")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Exit")

    try:
        #Input
        userDecision = int(input("\nEnter your choice: "))

        #Process
        if userDecision == 1:
            displayBooks()

        elif userDecision == 2:
            borrowBook()
        elif userDecision == 3:
            returnBook()
        elif userDecision == 4:

            #Output
            print("Thank you for using Jacob Library Online Catalogue!")
            print("Goodbye!")
        else:
            print("\nPlease enter a valid menu option 1-4.")

    except ValueError:
        print("Please enter a valid menu option 1-4.")






