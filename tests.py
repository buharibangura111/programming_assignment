
from operations import (
    add_book, add_member, borrow_book, return_book, delete_book, delete_member,
    search_books, update_book, update_member, find_member,
    books, members, GENRES
)

def reset_data():
    """Reset data structures for clean testing"""
    books.clear()
    members.clear()

def test_book_operations():
    """Test 1: Book CRUD operations"""
    reset_data()
    
    # Test add_book with valid genre
    assert add_book("978-1111111111", "Test Book", "Test Author", "Fiction", 3) is True
    assert "978-1111111111" in books
    assert books["978-1111111111"]["available_copies"] == 3
    
    # Test duplicate ISBN rejection
    assert add_book("978-1111111111", "Another Book", "Another Author", "Fiction", 2) is False
    
    # Test invalid genre rejection
    assert add_book("978-2222222222", "Invalid Genre Book", "Author", "InvalidGenre", 1) is False
    
    # Test search_books
    results = search_books("Test")
    assert len(results) == 1
    assert results[0]["title"] == "Test Book"
    
    # Test update_book
    assert update_book("978-1111111111", title="Updated Test Book") is True
    assert books["978-1111111111"]["title"] == "Updated Test Book"
    
    print("✓ Test 1: Book operations passed")

def test_member_operations():
    """Test 2: Member CRUD operations"""
    reset_data()
    
    # Test add_member
    assert add_member("M001", "John Doe", "john@example.com") is True
    assert len(members) == 1
    
    # Test duplicate member ID rejection
    assert add_member("M001", "Jane Doe", "jane@example.com") is False
    
    # Test find_member
    member = find_member("M001")
    assert member is not None
    assert member["name"] == "John Doe"
    
    # Test update_member
    assert update_member("M001", name="John Smith", email="johnsmith@example.com") is True
    assert members[0]["name"] == "John Smith"
    assert members[0]["email"] == "johnsmith@example.com"
    
    print("✓ Test 2: Member operations passed")

def test_borrow_return_operations():
    """Test 3: Borrow and return operations"""
    reset_data()
    
    # Setup
    add_book("978-3333333333", "Borrowable Book", "Author", "Fiction", 2)
    add_member("M002", "Borrower", "borrower@example.com")
    
    # Test successful borrow
    assert borrow_book("M002", "978-3333333333") is True
    assert books["978-3333333333"]["available_copies"] == 1
    assert "978-3333333333" in members[0]["borrowed_books"]
    
    # Test borrow when no copies available
    borrow_book("M002", "978-3333333333")  # Borrow second copy
    assert borrow_book("M002", "978-3333333333") is False  # Should fail - no copies left
    
    # Test return book
    assert return_book("M002", "978-3333333333") is True
    assert books["978-3333333333"]["available_copies"] == 1
    assert len(members[0]["borrowed_books"]) == 1
    
    print("✓ Test 3: Borrow/return operations passed")

def test_borrow_limit():
    """Test 4: Maximum borrow limit (3 books)"""
    reset_data()
    
    # Setup multiple books and one member
    for i in range(5):
        add_book(f"978-444444444{i}", f"Book {i}", "Author", "Fiction", 1)
    add_member("M003", "Heavy Borrower", "heavy@example.com")
    
    # Borrow 3 books (should succeed)
    for i in range(3):
        assert borrow_book("M003", f"978-444444444{i}") is True
    
    # Try to borrow 4th book (should fail due to limit)
    assert borrow_book("M003", "978-4444444443") is False
    
    # Verify member has exactly 3 books
    member = find_member("M003")
    assert len(member["borrowed_books"]) == 3
    
    print("✓ Test 4: Borrow limit enforcement passed")

def test_delete_operations():
    """Test 5: Delete operations with constraints"""
    reset_data()
    
    # Setup
    add_book("978-5555555555", "Deletable Book", "Author", "Fiction", 1)
    add_member("M004", "Deletable Member", "delete@example.com")
    
    # Test delete book with borrowed copies (should fail)
    borrow_book("M004", "978-5555555555")
    assert delete_book("978-5555555555") is False
    
    # Test delete member with borrowed books (should fail)
    assert delete_member("M004") is False
    
    # Return book and then delete should work
    return_book("M004", "978-5555555555")
    assert delete_book("978-5555555555") is True
    assert "978-5555555555" not in books
    
    # Now delete member should work
    assert delete_member("M004") is True
    assert find_member("M004") is None
    
    print("✓ Test 5: Delete operations with constraints passed")

def test_edge_cases():
    """Test 6: Edge cases and error handling"""
    reset_data()
    
    # Test operations on non-existent items
    assert borrow_book("NONEXISTENT", "NONEXISTENT") is False
    assert return_book("NONEXISTENT", "NONEXISTENT") is False
    assert update_book("NONEXISTENT", title="New Title") is False
    assert update_member("NONEXISTENT", name="New Name") is False
    assert delete_book("NONEXISTENT") is False
    assert delete_member("NONEXISTENT") is False
    
    # Test return book not borrowed
    add_book("978-6666666666", "Not Borrowed", "Author", "Fiction", 1)
    add_member("M005", "Member", "member@example.com")
    assert return_book("M005", "978-6666666666") is False
    
    print(" Test 6: Edge cases passed")

def run_all_tests():
    """Run all test functions"""
    print("Running Library Management System Tests...\n")
    
    test_book_operations()
    test_member_operations()
    test_borrow_return_operations()
    test_borrow_limit()
    test_delete_operations()
    test_edge_cases()
    
    print("\n All tests passed successfully!")
    print(f"Total genres available: {len(GENRES)} - {GENRES}")

if __name__ == "__main__":
    run_all_tests()
