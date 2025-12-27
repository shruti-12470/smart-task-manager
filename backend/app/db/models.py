import uuid
from sqlalchemy import Column, String, Text, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.sql import func
from .session import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(Text, nullable=False)
    description = Column(Text)
    category = Column(String)
    priority = Column(String)
    status = Column(String, default="pending")
    assigned_to = Column(String)
    due_date = Column(DateTime)
    extracted_entities = Column(JSONB)
    suggested_actions = Column(JSONB)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())


class TaskHistory(Base):
    __tablename__ = "task_history"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    task_id = Column(UUID(as_uuid=True), ForeignKey("tasks.id"))
    action = Column(String)
    old_value = Column(JSONB)
    new_value = Column(JSONB)
    changed_by = Column(String)
    changed_at = Column(DateTime(timezone=True), server_default=func.now())