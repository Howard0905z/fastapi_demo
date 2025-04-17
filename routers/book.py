from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.book import Book
from schemas.book import BookSchema,BookCreate, BookUpdate
from typing import List, Optional
from crud import book as crud

router = APIRouter()

# 1. POST /books
@router.post("/books", response_model=BookSchema)
def add_book(book: BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db, book)

# 2. GET /books?author=...&skip=0&limit=10
@router.get("/books", response_model=List[BookSchema])
def list_books(
    skip: int = 0,
    limit: int = 10,
    author: Optional[str] = None,
    db: Session = Depends(get_db)
):
    return crud.get_books(db, skip=skip, limit=limit, author=author)

# 3. PUT /books/{id}
@router.put("/books/{book_id}", response_model=BookSchema)
def edit_book(book_id: int, update: BookUpdate, db: Session = Depends(get_db)):
    updated_book = crud.update_book(db, book_id, update)
    if not updated_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated_book