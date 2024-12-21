# Day 24: Basic Library Management System

## **Project Overview**

Create a simple library management system using Python. The system should allow users to perform basic operations such as viewing available books, borrowing books, returning books, and adding new books. This project will help reinforce your understanding of functions, lists, and dictionaries in Python.

---

## **Features to Implement**

### 1. **View Available Books**
Write a function to display all the books currently available in the library.

```python
# Sample Output:
# Available Books:
# - The Great Gatsby
# - To Kill a Mockingbird
```

### 2. **Borrow a Book**
Allow users to borrow a book if it is available. If the book is not available, display an appropriate message.

```python
# Snippet:
def borrow_book(book_name):
    # Check if the book is available in the library
    # If available, remove it from the available books list
    # Otherwise, notify the user
```

### 3. **Return a Book**
Enable users to return a book they previously borrowed. Add the book back to the library.

```python
# Snippet:
def return_book(book_name):
    # Add the book back to the available books list
    # Notify the user of a successful return
```

### 4. **Add a New Book**
Allow the library admin to add new books to the library’s collection.

```python
# Snippet:
def add_book(book_name):
    # Add the new book to the library's collection
    # Notify the admin of the successful addition
```

---

## **System Workflow**

1. Initialize the library with a predefined list of books.
2. Display a menu to the user with the following options:
   - View Available Books
   - Borrow a Book
   - Return a Book
   - Add a New Book
   - Exit
3. Based on the user’s choice, call the appropriate function to perform the operation.

---

## **Example Interaction**

**Step 1**: User views available books.

```plaintext
Available Books:
- 1984
- Brave New World
- The Catcher in the Rye
```

**Step 2**: User chooses to borrow "1984".

```plaintext
You have borrowed "1984". Please return it within 14 days.
```

**Step 3**: User views available books again.

```plaintext
Available Books:
- Brave New World
- The Catcher in the Rye
```

**Step 4**: User returns "1984".

```plaintext
Thank you for returning "1984".
```

**Step 5**: User adds a new book "Moby Dick".

```plaintext
"Moby Dick" has been added to the library.
```

---

## **Hints and Suggestions**

1. Use a **list** to store the collection of books.
2. Use functions to modularize each operation.
3. Use a **while loop** to continuously display the menu until the user decides to exit.
4. Handle edge cases, such as:
   - Borrowing a book that is not available.
   - Returning a book that was not borrowed.

---

## **Conclusion**

This project is designed to provide a hands-on experience with functions, lists, and basic user input handling in Python. By completing this task, you'll gain practical skills in designing a simple, interactive system that can be further enhanced with additional features in the future.
