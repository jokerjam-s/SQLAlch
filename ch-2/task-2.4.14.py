from enum import Enum

from sqlalchemy import Column, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class TaskUrgency(Enum):
    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'


class Base(DeclarativeBase):
    pass


class TodoItem(Base):
    __tablename__ = 'todo_items'
    id: Mapped[int] = mapped_column(primary_key=True)
    urgency: Mapped[TaskUrgency] = mapped_column()
    title: Mapped[str] = mapped_column(String(200))