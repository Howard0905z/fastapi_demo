from pydantic import BaseModel
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

app = FastAPI()

class UserCreate(BaseModel):
    name: str
    email: str
    age: int
    phone: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

class Item(BaseModel):
    id: int
    name: str

def api_response(data=None, message="Success", status="success", code=200):
    return JSONResponse(
        status_code=code,
        content={
            "status": status,
            "message": message,
            "data": data
        }
    )

@app.exception_handler(RequestValidationError)
def validation_exception_handler(request: Request, exc: RequestValidationError):
    error_messages = [e['msg'] for e in exc.errors()]
    return JSONResponse(
        status_code=422,
        #content={"status": "error", "message": "格式錯誤", "detail": exc.errors()},
        content={"status": "error", "message": "資料格式錯誤", "errors": error_messages},
    )


@app.post("/users")
def create_user(user: UserCreate):
    return {"message": "User created", "user": user}


"""
@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    return {
        "id": user_id,
        "name": "Alice",
        "email": "alice@example.com",
        "password": "123456"  # 不會被回傳，因為不在 model 裡
    }
    

"""
@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id != 1:
        raise HTTPException(status_code=404, detail="User not found")
    return {"id": user_id, "name": "Alice"}




@app.get("/standard")
def standard_response():
    return JSONResponse(
        content={
            "status": "success",
            "message": "Data fetched successfully",
            "data": {"value": 123}
        }
    )

@app.get("/standard_json")
def standard_response():
    return api_response(
        data={"value": 123},
        message="Data fetched successfully"
    )

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    return {"id": item_id, "name": "Example"}

#練習
def user_api_response(data=None, message="Success", status="success", code=200):
    return JSONResponse(
        status_code=code,
        content={
            "status": status,
            "message": message,
            "data": data
        }
    )

# 登入請求模型
class LoginRequest(BaseModel):
    email: str
    password: str

# 登入回傳模型（不含密碼）
class UserResponse(BaseModel):
    name: str
    email: str
    
# 單一硬編碼帳號密碼
HARD_CODED_EMAIL = "test@example.com"
HARD_CODED_PASSWORD = "123456"
HARD_CODED_NAME = "Test User"

@app.post("/login")
def login(data: LoginRequest):
    if data.email != HARD_CODED_EMAIL or data.password != HARD_CODED_PASSWORD:
        raise HTTPException(status_code=401, detail="帳號或密碼錯誤")

    user = UserResponse(name=HARD_CODED_NAME, email=data.email)
    return user_api_response(
        data=user.dict(),
        message="User fetched"
    )