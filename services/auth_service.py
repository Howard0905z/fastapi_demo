from sqlalchemy.orm import Session
from models.user import User
from schemas.user_create import UserCreate
from utils.auth import hash_password
from fastapi import HTTPException

def register_user(db: Session, user: UserCreate):
    # 檢查是否已註冊
    existing = db.query(User).filter(User.email == user.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = User(
        email=user.email,
        hashed_password=hash_password(user.password),
        is_active=True,
        is_admin=False  # 預設不是管理員
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
