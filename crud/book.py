from sqlalchemy.orm import Session
from models.book import Book
from schemas.book import BookCreate, BookUpdate
from typing import List, Optional

def create_book(db: Session, book: BookCreate) -> Book:
    new_book = Book(**book.dict())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

def get_books(db: Session, skip: int = 0, limit: int = 10, author: Optional[str] = None) -> List[Book]:
    query = db.query(Book)
    if author:
        query = query.filter(Book.author.ilike(f"%{author}%"))
    return query.offset(skip).limit(limit).all()

def update_book(db: Session, book_id: int, update_data: BookUpdate) -> Optional[Book]:
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        return None
    for key, value in update_data.dict(exclude_unset=True).items():
        setattr(book, key, value)
    db.commit()
    db.refresh(book)
    return book
