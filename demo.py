#!/usr/bin/env python3
"""
Demo Script for Mini Library Management System
Limkokwing University - PROG211 Assignment 1

This script demonstrates all the core functionality of the library system:
- Adding books and members
- Searching and updating records
- Borrowing and returning books
- Deleting records with proper constraints
- Error handling and edge cases
"""

from operations import (
    add_book, add_member, search_books, borrow_book, return_book,
    update_book, update_member, delete_book, delete_member, find_member,
    books, members, GENRES
)
from data import books as initial_books, members as initial_members

def print_separator(title):
    """Print a formatted section separator"""
    print(f"\n{'='*50}")
    print(f" {title}")
    print(f"{'='*50}")

def print_books():
    """Display all books in the system"""
    print("\nCurrent Books in Library:")
    if not books:
        print("  No books in the system.")
        return
    
    for isbn, book in books.items():
        print(f"  ISBN: {isbn}")
        print(f"    Title: {book['title']}")
        print(f"    Author: {book['author']}")
        print(f"    Genre: {book['genre']}")
        print(f"    Copies: {book['available_copies']}/{book['total_copies']} available")
        print()

def print_members():
    """Display all members in the system"""
    print("\nCurrent Library Members:")
    if not members:
        print("  No members in the system.")
        return
    
    for member in members:
        print(f"  ID: {member['member_id']}")
        print(f"    Name: {member['name']}")
        print(f"    Email: {member['email']}")
        print(f"    Borrowed Books: {len(member['borrowed_books'])} books")
        if member['borrowed_books']:
            for isbn in member['borrowed_books']:
                if isbn in books:
                    print(f"      - {books[isbn]['title']} ({isbn})")
        print()

def demo_system_overview():
    """Show initial system state"""
    print_separator("SYSTEM OVERVIEW")
    print(f"Available Genres: {GENRES}")
    print_books()
    print_members()

def demo_adding_records():
    """Demonstrate adding books and members"""
    print_separator("ADDING NEW RECORDS")
    
    # Add new books
    print("Adding new books...")
    success = add_book("978-9999999999", "Advanced Python Programming", "Mark Gbla", "Non-Fiction", 3)
    print(f"✓ Added 'Advanced Python Programming': {success}")
    
    success = add_book("978-8888888888", "The Future of AI", "Dr. Smith", "Sci-Fi", 2)
    print(f"✓ Added 'The Future of AI': {success}")
    
    # Try to add book with invalid genre
    success = add_book("978-7777777777", "Invalid Book", "Author", "InvalidGenre", 1)
    print(f"✗ Tried to add book with invalid genre: {success}")
    
    # Add new members
    print("\nAdding new members...")
    success = add_member("M100", "Alice Johnson", "alice@limkokwing.edu.sl")
    print(f"✓ Added member Alice Johnson: {success}")
    
    success = add_member("M101", "Bob Wilson", "bob@limkokwing.edu.sl")
    print(f"✓ Added member Bob Wilson: {success}")
    
    # Try to add duplicate member
    success = add_member("M100", "Charlie Brown", "charlie@limkokwing.edu.sl")
    print(f"✗ Tried to add duplicate member ID: {success}")

def demo_searching_updating():
    """Demonstrate search and update functionality"""
    print_separator("SEARCHING AND UPDATING")
    
    # Search books
    print("Searching for books containing 'Python':")
    results = search_books("Python")
    for book in results:
        print(f"  Found: {book['title']} by {book['author']} (ISBN: {book['isbn']})")
    
    print("\nSearching for books by 'Douglas Adams':")
    results = search_books("Douglas Adams")
    for book in results:
        print(f"  Found: {book['title']} by {book['author']} (ISBN: {book['isbn']})")
    
    # Update book information
    print("\nUpdating book information...")
    success = update_book("978-9999999999", title="Expert Python Programming", total_copies=5)
    print(f"✓ Updated 'Advanced Python Programming': {success}")
    if success:
        book = books["978-9999999999"]
        print(f"  New title: {book['title']}")
        print(f"  New total copies: {book['total_copies']}")
    
    # Update member information
    print("\nUpdating member information...")
    success = update_member("M100", name="Alice Johnson-Smith", email="alice.smith@limkokwing.edu.sl")
    print(f"✓ Updated member M100: {success}")
    if success:
        member = find_member("M100")
        print(f"  New name: {member['name']}")
        print(f"  New email: {member['email']}")

def demo_borrowing_returning():
    """Demonstrate borrowing and returning books"""
    print_separator("BORROWING AND RETURNING BOOKS")
    
    # Successful borrowing
    print("Alice (M100) borrowing books...")
    success = borrow_book("M100", "978-9999999999")
    print(f"✓ Borrowed 'Expert Python Programming': {success}")
    
    success = borrow_book("M100", "978-0545010221")
    print(f"✓ Borrowed 'The Hitchhiker's Guide to the Galaxy': {success}")
    
    success = borrow_book("M100", "978-8888888888")
    print(f"✓ Borrowed 'The Future of AI': {success}")
    
    # Show member's borrowed books
    member = find_member("M100")
    print(f"\nAlice now has {len(member['borrowed_books'])} books borrowed")
    
    # Try to borrow 4th book (should fail due to limit)
    success = borrow_book("M100", "978-0451450493")
    print(f"✗ Tried to borrow 4th book (limit is 3): {success}")
    
    # Bob borrowing the same book Alice has
    print("\nBob (M101) trying to borrow a book...")
    success = borrow_book("M101", "978-8888888888")
    print(f"✗ Bob tried to borrow 'The Future of AI' (no copies left): {success}")
    
    success = borrow_book("M101", "978-0451450493")
    print(f"✓ Bob borrowed 'The Art of Computer Programming': {success}")
    
    # Return books
    print("\nAlice returning a book...")
    success = return_book("M100", "978-8888888888")
    print(f"✓ Alice returned 'The Future of AI': {success}")
    
    # Now Bob can borrow it
    success = borrow_book("M101", "978-8888888888")
    print(f"✓ Bob can now borrow 'The Future of AI': {success}")

def demo_deletion_constraints():
    """Demonstrate deletion with proper constraints"""
    print_separator("DELETION WITH CONSTRAINTS")
    
    # Try to delete a book that's currently borrowed
    print("Trying to delete books and members with constraints...")
    success = delete_book("978-9999999999")  # Alice has this book
    print(f"✗ Tried to delete book currently borrowed: {success}")
    
    # Try to delete member with borrowed books
    success = delete_member("M100")  # Alice has borrowed books
    print(f"✗ Tried to delete member with borrowed books: {success}")
    
    # Return all books first
    print("\nAlice returning all borrowed books...")
    member = find_member("M100")
    borrowed_books = member['borrowed_books'].copy()  # Make a copy to avoid modification during iteration
    for isbn in borrowed_books:
        success = return_book("M100", isbn)
        if success and isbn in books:
            print(f"✓ Returned: {books[isbn]['title']}")
    
    # Now deletion should work
    print("\nNow trying deletions again...")
    success = delete_book("978-9999999999")
    print(f"✓ Deleted book (no longer borrowed): {success}")
    
    success = delete_member("M100")
    print(f"✓ Deleted member (no borrowed books): {success}")

def demo_error_handling():
    """Demonstrate error handling for invalid operations"""
    print_separator("ERROR HANDLING")
    
    print("Testing operations with invalid data...")
    
    # Non-existent member/book operations
    success = borrow_book("INVALID_ID", "978-0545010221")
    print(f"✗ Borrow with invalid member ID: {success}")
    
    success = borrow_book("M101", "INVALID_ISBN")
    print(f"✗ Borrow with invalid ISBN: {success}")
    
    success = return_book("M101", "978-0545010221")  # Bob never borrowed this
    print(f"✗ Return book never borrowed: {success}")
    
    success = update_book("INVALID_ISBN", title="New Title")
    print(f"✗ Update non-existent book: {success}")
    
    success = update_member("INVALID_ID", name="New Name")
    print(f"✗ Update non-existent member: {success}")

def main():
    """Main demo function"""
    print("🏛️  MINI LIBRARY MANAGEMENT SYSTEM DEMO")
    print("   Limkokwing University - PROG211 Assignment 1")
    print("   Developed by: Mark Gbla")
    
    # Run all demo sections
    demo_system_overview()
    demo_adding_records()
    demo_searching_updating()
    demo_borrowing_returning()
    demo_deletion_constraints()
    demo_error_handling()
    
    # Final system state
    print_separator("FINAL SYSTEM STATE")
    print_books()
    print_members()
    
    print("\n🎉 Demo completed successfully!")
    print("\nKey Features Demonstrated:")
    print("✓ Dictionary-based book storage with ISBN keys")
    print("✓ List-based member management")
    print("✓ Tuple-based genre validation")
    print("✓ CRUD operations for books and members")
    print("✓ Borrowing/returning with proper constraints")
    print("✓ Search functionality")
    print("✓ Error handling and validation")
    print("✓ Maximum borrow limit enforcement (3 books)")
    print("✓ Deletion constraints (no borrowed items)")

if __name__ == "__main__":
    main()
