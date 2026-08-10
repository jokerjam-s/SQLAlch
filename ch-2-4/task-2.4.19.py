import uuid
from datetime import datetime
from enum import Enum

from sqlalchemy import Enum as SAEnum, JSON, Boolean, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class ChangeType(Enum):
    CREATE = 'create'
    UPDATE = 'update'
    DELETE = 'delete'


class Base(DeclarativeBase):
    pass


class ChangeLogEntry(Base):
    __tablename__ = 'change_log_entries'
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    change_type: Mapped[ChangeType] = mapped_column(SAEnum(ChangeType))
    entity_payload: Mapped[dict] = mapped_column(JSON)
    is_success: Mapped[bool] = mapped_column(Boolean)
    created_at: Mapped[datetime] = mapped_column(DateTime)