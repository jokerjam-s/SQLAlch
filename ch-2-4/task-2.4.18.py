import uuid
from datetime import datetime
from enum import Enum

from sqlalchemy import Enum as SAEnum, JSON, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class ProcessStatus(Enum):
    NEW = 'new'
    PROCESSED = 'processed'
    FAILED = 'failed'


class Base(DeclarativeBase):
    pass

class EventQueueItem(Base):
    __tablename__ = 'event_queue_items'

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    status: Mapped[ProcessStatus] = mapped_column(SAEnum(ProcessStatus))
    payload: Mapped[dict] = mapped_column(JSON)
    created_at: Mapped[datetime] = mapped_column(DateTime)