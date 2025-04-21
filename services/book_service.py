from sqlalchemy.orm import Session
from crud.book import get_books, create_book, update_book
from typing import Optional

def list_books_service(db: Session, skip: int = 0, limit: int = 10, author: Optional[str] = None):
    return get_books(db, skip=skip, limit=limit, author=author)

def create_book_service(db: Session, book_data):
    return create_book(db, book_data)