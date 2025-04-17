from fastapi import APIRouter, Depends, HTTPException
from typing import Optional
from sqlalchemy import asc, desc, or_
from sqlalchemy.orm import Session
from database import get_db
from schemas.user import UserSchema
from schemas.user_create import UserCreate
from schemas.user_update import UserUpdate
from crud import user as crud
from typing import List
from models.user import User
from services.user_service import list_users_service

router = APIRouter()

@router.get("/users", response_model=List[UserSchema])
def list_users(db: Session = Depends(get_db)):
    return list_users_service(db)

@router.get("/users_search", response_model=List[UserSchema])
def get_users(
    skip: int = 0,
    limit: int = 10,
    age: Optional[int] = None,
    search: Optional[str] = None,               
    sort_by: Optional[str] = "id",             
    sort_order: Optional[str] = "asc",          
    db: Session = Depends(get_db)
):
    query = db.query(User)

    # 年齡篩選
    if age is not None:
        query = query.filter(User.age == age)

    # 模糊搜尋（這邊以 name 和 email 為例）
    if search:
        query = query.filter(
            or_(
                User.name.ilike(f"%{search}%"),
                User.email.ilike(f"%{search}%")
            )
        )

    # 排序邏輯
    sort_column = getattr(User, sort_by, None)
    if sort_column:
        if sort_order.lower() == "desc":
            query = query.order_by(desc(sort_column))
        else:
            query = query.order_by(asc(sort_column))
    else:
        query = query.order_by(User.id.asc())  # 預設排序

    return query.offset(skip).limit(limit).all()

@router.get("/users/{user_id}", response_model=UserSchema)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/users", response_model=UserSchema)
def add_user(user: UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

@router.put("/users/{user_id}", response_model=UserSchema)
def edit_user(user_id: int, update: UserUpdate, db: Session = Depends(get_db)):
    return crud.update_user(db, user_id, update.dict(exclude_unset=True))

@router.delete("/users/{user_id}")
def remove_user(user_id: int, db: Session = Depends(get_db)):
    crud.delete_user(db, user_id)
    return {"message": "User deleted"}
