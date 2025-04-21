from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dependencies.auth import get_current_admin_user
from database import get_db
from services.user_service import delete_user_by_id
from models.user import User

router = APIRouter()

@router.delete("/users/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin_user)
):
    return delete_user_by_id(db, user_id)


@router.get("/admin/dashboard")
def admin_dashboard(current_user: User = Depends(get_current_admin_user)):
    return {
        "message": "歡迎來到管理員專區",
        "admin": current_user.email
    }