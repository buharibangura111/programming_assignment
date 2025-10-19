# Mini Library Management System

**Limkokwing University - PROG211 Assignment 1**  
**Student:** Buhari Bangura  
**Semester:** 3 (September 2025 - February 2026)

## Overview

A simple Library Management System built with Python using dictionaries, lists, and tuples. Manages books, members, and borrowing operations with proper validation.

## Features

- Add, search, update, and delete books
- Register and manage library members  
- Borrow and return books (max 3 per member)
- Search books by title or author
- Data validation and error handling

## Files

```
├── data.py       # Sample data
├── operations.py # Main functions
├── demo.py      # Demo script
├── tests.py     # Unit tests
└── README.md    # This file
```

## How to Run

### Step 1: Check Python
Make sure Python 3.6+ is installed:
```bash
python --version
```

### Step 2: Run the Demo
```bash
python demo.py
```
This shows all features working with sample data.

### Step 3: Run Tests
```bash
python tests.py
```
This runs 6 test suites to verify everything works.

### Step 4: Use Interactively
```python
from operations import *

# Add a book
add_book("978-1234567890", "Python Guide", "John Doe", "Non-Fiction", 3)

# Add a member
add_member("M001", "Alice Smith", "alice@example.com")

# Borrow a book
borrow_book("M001", "978-1234567890")

# Search books
results = search_books("Python")
```

## Main Functions

### Books
- `add_book(isbn, title, author, genre, copies)` - Add new book
- `search_books(query)` - Find books by title/author
- `update_book(isbn, **kwargs)` - Update book info
- `delete_book(isbn)` - Remove book (if not borrowed)

### Members
- `add_member(id, name, email)` - Register new member
- `find_member(id)` - Find member by ID
- `update_member(id, **kwargs)` - Update member info
- `delete_member(id)` - Remove member (if no borrowed books)

### Borrowing
- `borrow_book(member_id, isbn)` - Borrow book (max 3 per member)
- `return_book(member_id, isbn)` - Return borrowed book

## Data Structures Used

- **Dictionary**: Books storage (ISBN as key)
- **List**: Members storage  
- **Tuple**: Valid genres ("Fiction", "Non-Fiction", "Sci-Fi", etc.)

## Assignment Requirements 

- **Dictionary (20 marks)**: Books with ISBN keys
- **Lists (15 marks)**: Members in list format
- **Tuples (15 marks)**: Immutable genres
- **CRUD Operations (25 marks)**: All functions implemented
- **Documentation (25 marks)**: README, comments, tests

---

**Developer:** Buhari Bangura  
**Course:** PROG211 - Object-Oriented Programming 1  
**Limkokwing University of Creative Technology**
