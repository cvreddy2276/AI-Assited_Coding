'''		Task 7 – Refactoring the Library Management System
Problem Statement
You are provided with a poorly structured Library Management script that:
•	Contains repeated conditional logic
•	Does not use reusable functions
•	Lacks documentation
•	Uses print-based procedural execution
•	Does not follow modular programming principles
Your task is to refactor the code into a proper format 
1.	Create a module library.py with functions:
o	add_book(title, author, isbn)
o	remove_book(isbn)
o	search_book(isbn)
2.	Insert triple quotes under each function and let Copilot complete the docstrings.
3.	Generate documentation in the terminal.
4.	Export the documentation in HTML format.
5.	Open the file in a browser.
Given Code 
# Library Management System (Unstructured Version)
# This code needs refactoring into a proper module with documentation.
library_db = {}
# Adding first book
title = "Python Basics"
author = "John Doe"
isbn = "101"

if isbn not in library_db:
    library_db[isbn] = {"title": title, "author": author}
    print("Book added successfully.")
else:
    print("Book already exists.")

# Adding second book (duplicate logic)
title = "AI Fundamentals"
author = "Jane Smith"
isbn = "102"

if isbn not in library_db:
    library_db[isbn] = {"title": title, "author": author}
    print("Book added successfully.")
else:
    print("Book already exists.")

# Searching book (repeated logic structure)
isbn = "101"
if isbn in library_db:
    print("Book Found:", library_db[isbn])
else:
    print("Book not found.")

# Removing book (again repeated pattern)
isbn = "101"
if isbn in library_db:
    del library_db[isbn]
    print("Book removed successfully.")
else:
    print("Book not found.")

# Searching again
isbn = "101"
if isbn in library_db:
    print("Book Found:", library_db[isbn])
else:
    print("Book not found.")
		
'''

# Refactored Library Management System (Structured Version)
# library.py
library_db = {}
def add_book(title, author, isbn):
    """
    Add a book to the library database.
    Parameters:
    title (str): The title of the book.
    author (str): The author of the book.
    isbn (str): The ISBN number of the book.
    Returns:
    str: A message indicating whether the book was added successfully or if it already exists.
    """
    if isbn not in library_db:
        library_db[isbn] = {"title": title, "author": author}
        return "Book added successfully."
    else:
        return "Book already exists."
def remove_book(isbn):
    """
    Remove a book from the library database.
    Parameters:isbn (str): The ISBN number of the book to be removed.
    Returns:
    str: A message indicating whether the book was removed successfully or if it was not found.
    """
    if isbn in library_db:
        del library_db[isbn]
        return "Book removed successfully."
    else:
        return "Book not found."
def search_book(isbn):
    """
    Search for a book in the library database.
    Parameters:isbn (str): The ISBN number of the book to search for.
    Returns:
    str: A message indicating whether the book was found along with its details, or if it was not found.
    """
    if isbn in library_db:
        return f"Book Found: {library_db[isbn]}"
    else:
        return "Book not found."
# Example usage of the library module
if __name__ == "__main__":
    print(add_book("Python Basics", "John Doe", "101"))
    print(add_book("AI Fundamentals", "Jane Smith", "102"))
    print(search_book("101"))
    print(remove_book("101"))
    print(search_book("101"))

    