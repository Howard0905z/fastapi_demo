from sqlalchemy.orm import Session
from fastapi import HTTPException
from schemas.task import TaskCreate, TaskUpdate
from crud import task as crud

def create_task_service(db: Session, task_data: TaskCreate):
    return crud.create_task(db, task_data)

def list_tasks_service(db: Session):
    return crud.get_tasks(db)

def get_task_service(db: Session, task_id: int):
    task = crud.get_task_by_id(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

def update_task_service(db: Session, task_id: int, update_data: TaskUpdate):
    updated_task = crud.update_task(db, task_id, update_data)
    if not updated_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task

def delete_task_service(db: Session, task_id: int):
    deleted = crud.delete_task(db, task_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted"}
