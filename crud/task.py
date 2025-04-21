from sqlalchemy.orm import Session
from models.task import Task
from schemas.task import TaskCreate, TaskUpdate
from typing import List, Optional

def create_task(db: Session, task: TaskCreate) -> Task:
    new_task = Task(**task.dict())
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

def get_tasks(db: Session) -> List[Task]:
    return db.query(Task).all()

def get_task_by_id(db: Session, task_id: int) -> Optional[Task]:
    return db.query(Task).filter(Task.id == task_id).first()

def update_task(db: Session, task_id: int, update_data: TaskUpdate) -> Optional[Task]:
    task = get_task_by_id(db, task_id)
    if not task:
        return None
    for key, value in update_data.dict(exclude_unset=True).items():
        setattr(task, key, value)
    db.commit()
    db.refresh(task)
    return task

def delete_task(db: Session, task_id: int) -> bool:
    task = get_task_by_id(db, task_id)
    if not task:
        return False
    db.delete(task)
    db.commit()
    return True
