from pydantic import BaseModel
from typing import Optional

class BookCreate(BaseModel):
    title: str
    author: str
    price: float

class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    price: Optional[float] = None

#response model
class BookSchema(BaseModel):
    id: int
    title: str
    author: str
    price: float

    class Config:
        orm_mode = True
        # 這個設定讓 Pydantic 可以從 ORM 模型轉換成 Pydantic 模型
