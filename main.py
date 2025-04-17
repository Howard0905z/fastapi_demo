from fastapi import FastAPI
from routers import user, book
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS 設定（如果你有前端要串）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 可限制前端來源
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 註冊路由
app.include_router(user.router, tags=["Users"])
app.include_router(book.router, tags=["Books"])

@app.get("/")
def root():
    return {"message": "Welcome to the API!"}


