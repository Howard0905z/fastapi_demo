from sqlalchemy.orm import Session
from crud.user import get_users
from fastapi import HTTPException
from models.user import User

def list_users_service(db: Session):
    return get_users(db)


def delete_user_by_id(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="使用者不存在")

    db.delete(user)
    db.commit()
    return {"message": f"使用者 {user.email} 已刪除"}