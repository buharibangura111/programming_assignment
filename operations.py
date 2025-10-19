# operations.py

from typing import Dict, List, Tuple, Optional
from data import books, members, GENRES

# ---------- Book functions ----------
def add_book(isbn: str, title: str, author: str, genre: str, total_copies: int) -> bool:
    if isbn in books:
        return False  # ISBN must be unique
    if genre not in GENRES:
        return False
    books[isbn] = {
        "title": title,
        "author": author,
        "genre": genre,
        "total_copies": int(total_copies),
        "available_copies": int(total_copies)
    }
    return True

def search_books(query: str) -> List[Dict]:
    q = query.lower()
    results = []
    for isbn, info in books.items():
        if q in info["title"].lower() or q in info["author"].lower():
            row = info.copy()
            row["isbn"] = isbn
            results.append(row)
    return results

def update_book(isbn: str, **kwargs) -> bool:
    if isbn not in books:
        return False
    book = books[isbn]
    # Allowed updates: title, author, genre, total_copies
    if "genre" in kwargs and kwargs["genre"] not in GENRES:
        return False
    # handle total_copies change (maintain available_copies)
    if "total_copies" in kwargs:
        new_total = int(kwargs["total_copies"])
        diff = new_total - book["total_copies"]
        book["total_copies"] = new_total
        book["available_copies"] += diff
        if book["available_copies"] < 0:
            # cannot set total lower than borrowed count
            return False
    for key in ("title", "author", "genre"):
        if key in kwargs:
            book[key] = kwargs[key]
    return True

def delete_book(isbn: str) -> bool:
    if isbn not in books:
        return False
    if books[isbn]["available_copies"] != books[isbn]["total_copies"]:
        # some copies are currently borrowed
        return False
    del books[isbn]
    return True

# ---------- Member functions ----------
def add_member(member_id: str, name: str, email: str) -> bool:
    if any(m["member_id"] == member_id for m in members):
        return False
    members.append({"member_id": member_id, "name": name, "email": email, "borrowed_books": []})
    return True

def find_member(member_id: str) -> Optional[Dict]:
    for m in members:
        if m["member_id"] == member_id:
            return m
    return None

def update_member(member_id: str, **kwargs) -> bool:
    m = find_member(member_id)
    if not m:
        return False
    if "name" in kwargs:
        m["name"] = kwargs["name"]
    if "email" in kwargs:
        m["email"] = kwargs["email"]
    return True

def delete_member(member_id: str) -> bool:
    m = find_member(member_id)
    if not m:
        return False
    if m["borrowed_books"]:
        # cannot delete while member has borrowed books
        return False
    members.remove(m)
    return True

# ---------- Borrow / Return ----------
MAX_BORROW = 3

def borrow_book(member_id: str, isbn: str) -> bool:
    m = find_member(member_id)
    if not m or isbn not in books:
        return False
    if len(m["borrowed_books"]) >= MAX_BORROW:
        return False
    if books[isbn]["available_copies"] <= 0:
        return False
    # borrow
    m["borrowed_books"].append(isbn)
    books[isbn]["available_copies"] -= 1
    return True

def return_book(member_id: str, isbn: str) -> bool:
    m = find_member(member_id)
    if not m or isbn not in books:
        return False
    if isbn not in m["borrowed_books"]:
        return False
    m["borrowed_books"].remove(isbn)
    books[isbn]["available_copies"] += 1
    return True

