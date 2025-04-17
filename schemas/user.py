from pydantic import BaseModel

class UserSchema(BaseModel):
    id: int
    email: str
    name: str
    age: int

    class Config:
        orm_mode = True
        # 這個設定讓 Pydantic 可以從 ORM 模型轉換成 Pydantic 模型
