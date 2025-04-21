from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from utils.jwt import SECRET_KEY, ALGORITHM
from models.user import User
from sqlalchemy.orm import Session
from database import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Token 無效：缺少 user_id")
        user_id = int(user_id)
    except (JWTError, ValueError):
        raise HTTPException(status_code=401, detail="無效的 token")

    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="使用者不存在")

    return user


def get_current_admin_user(current_user: User = Depends(get_current_user)) -> User:
    print("目前登入者：", current_user.email, "| 管理員 =", current_user.is_admin)
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="需要管理員權限")
    return current_user

