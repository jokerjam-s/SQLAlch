from datetime import datetime

from sqlalchemy import String, SmallInteger, DateTime, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class TaskCard(Base):
    __tablename__ = 'task_cards'
    id: Mapped[int] = mapped_column(primary_key=True)
    headline: Mapped[str] = mapped_column(String(200))
    status: Mapped[str] = mapped_column(String(24), default='new')
    priority_rank: Mapped[int] = mapped_column(SmallInteger, default=1)
    opened_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    touched_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())

