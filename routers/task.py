from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from schemas.task import TaskSchema, TaskCreate, TaskUpdate
from services import task_service
from typing import List

router = APIRouter()

@router.post("/tasks", response_model=TaskSchema)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    return task_service.create_task_service(db, task)

@router.get("/tasks", response_model=List[TaskSchema])
def list_tasks(db: Session = Depends(get_db)):
    return task_service.list_tasks_service(db)

@router.get("/tasks/{task_id}", response_model=TaskSchema)
def get_task(task_id: int, db: Session = Depends(get_db)):
    return task_service.get_task_service(db, task_id)

@router.put("/tasks/{task_id}", response_model=TaskSchema)
def update_task(task_id: int, update: TaskUpdate, db: Session = Depends(get_db)):
    return task_service.update_task_service(db, task_id, update)

@router.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task_service.delete_task_service(db, task_id)
    return {"message": "Task deleted"}
