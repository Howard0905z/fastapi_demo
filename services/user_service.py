from sqlalchemy.orm import Session
from crud.user import get_users

def list_users_service(db: Session):
    return get_users(db)
