from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# PostgreSQL 連線字串
DATABASE_URL = "postgresql://xujiancheng:@localhost:5432/postgres"

engine = create_engine(DATABASE_URL)

# 建立 SessionLocal，每次操作資料庫用這個產生 session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 所有 ORM 類別的基底
Base = declarative_base()

def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()