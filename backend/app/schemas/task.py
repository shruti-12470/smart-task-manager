from pydantic import BaseModel
from typing import Optional, Dict, List
from datetime import datetime
from uuid import UUID


class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    assigned_to: Optional[str] = None
    due_date: Optional[datetime] = None


class TaskResponse(BaseModel):
    id:UUID
    title: str
    description: Optional[str]
    category: str
    priority: str
    status: str
    assigned_to: Optional[str]
    due_date: Optional[datetime]
    extracted_entities: Dict
    suggested_actions: List[str]

    class Config:
        orm_mode=True