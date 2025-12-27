from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db.models import Task
from app.schemas.task import TaskCreate, TaskResponse
from app.services.classifier import classify_task

router = APIRouter()


@router.post("/", response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    classification = classify_task(task.title, task.description)

    new_task = Task(
        title=task.title,
        description=task.description,
        category=classification["category"],
        priority=classification["priority"],
        extracted_entities=classification["extracted_entities"],
        suggested_actions=classification["suggested_actions"],
        assigned_to=task.assigned_to,
        due_date=task.due_date,
        status="pending",
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task

from typing import List
from app.schemas.task import TaskResponse


@router.get("/", response_model=List[TaskResponse])
def get_tasks(db: Session = Depends(get_db)):
    tasks = db.query(Task).all()
    return tasks