from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.post("/hello")
def say_hello():
    return {"message": "This is a POST request."}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/search/")
def search_items(keyword: str, limit: int = 10):
    return {"keyword": keyword, "limit": limit}

@app.post("/items/")
def create_item(item: Item):
    return {"item_name": item.name, "price": item.price, "in_stock": item.in_stock}
