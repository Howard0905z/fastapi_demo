from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from utils.jwt import create_access_token
from utils.auth import verify_password
from models.user import User
from database import get_db
from schemas.token import Token
from schemas.user import UserSchema
from dependencies.auth import get_current_user
from schemas.user_create import UserCreate
from services.auth_service import register_user

router = APIRouter()

@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    access_token = create_access_token(data={"sub": str(user.id)})
    return {"access_token": access_token}

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    registered = register_user(db, user)
    return {"message": "註冊成功", "user_id": registered.id}
