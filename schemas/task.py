from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    due_date: datetime

class TaskUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    due_date: Optional[datetime]
    is_completed: Optional[bool]

class TaskSchema(BaseModel):
    id: int
    title: str
    description: Optional[str]
    due_date: datetime
    is_completed: bool

    class Config:
        orm_mode = True


