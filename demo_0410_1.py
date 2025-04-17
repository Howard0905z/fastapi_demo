from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 使用者資料模型
class User(BaseModel):
    name: str
    email: str
    age: int

# 模擬資料庫
fake_users = {}

# 建立使用者
@app.post("/users")
def create_user(user: User):
    user_id = len(fake_users) + 1
    fake_users[user_id] = user
    return {"id": user_id, "user": user}

# 取得所有使用者
@app.get("/users")
def get_all_users():
    return fake_users

# 取得單一使用者
@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = fake_users.get(user_id)
    if not user:
        return {"error": "User not found"}
    return user

# 更新使用者
@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    if user_id not in fake_users:
        return {"error": "User not found"}
    fake_users[user_id] = user
    return {"id": user_id, "user": user}

# 刪除使用者
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    if user_id not in fake_users:
        return {"error": "User not found"}
    del fake_users[user_id]
    return {"message": f"User {user_id} deleted"}
