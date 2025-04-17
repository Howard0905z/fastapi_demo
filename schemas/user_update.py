from pydantic import BaseModel
from typing import Optional

class UserUpdate(BaseModel):
    name: Optional[str]
    email: Optional[str]
    age: Optional[int]
