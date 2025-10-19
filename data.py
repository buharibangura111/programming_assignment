# books: dict keyed by ISBN
books = {
    "978-0545010221": {
        "title": "The Hitchhiker's Guide to the Galaxy",
        "author": "Douglas Adams",
        "genre": "Sci-Fi",
        "total_copies": 10,
        "available_copies": 10
    },
    "978-0451450493": {
        "title": "The Art of Computer Programming",
        "author": "Donald Knuth",
        "genre": "Non-Fiction",
        "total_copies": 5,
        "available_copies": 5
    },
    "978-0141036146": {
        "title": "Sapiens: A Brief History of Humankind",
        "author": "Yuval Noah Harari",
        "genre": "Non-Fiction",
        "total_copies": 8,
        "available_copies": 8
    },
    "978-1455555988": {
        "title": "The Martian",
        "author": "Andy Weir",
        "genre": "Sci-Fi",
        "total_copies": 4,
        "available_copies": 4
    },
    "978-0345510366": {
        "title": "The Name of the Rose",
        "author": "Umberto Eco",
        "genre": "Fiction",
        "total_copies": 7,
        "available_copies": 7
    },
}

# members: list of dicts
members = [
    {"member_id": "M001", "name": "Kadio Kele", "email": "kele@example.com", "borrowed_books": []},
    {"member_id": "M002", "name": "Mama Kele", "email": "mama@example.com", "borrowed_books": []},
    {"member_id": "M003", "name": "Papa Kele", "email": "papa@example.com", "borrowed_books": []},
    {"member_id": "M004", "name": "Son Kele", "email": "son@example.com", "borrowed_books": []},
    {"member_id": "M005", "name": "Daughter Kele", "email": "daughter@example.com", "borrowed_books": []},
]

# genres: tuple (immutable, fixed set)
GENRES = ("Fiction", "Non-Fiction", "Sci-Fi", "Biography", "Mystery", "History", "Historical Fiction")
