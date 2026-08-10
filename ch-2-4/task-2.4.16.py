from datetime import datetime

from sqlalchemy import String, JSON, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class ActionHistory(Base):
    __tablename__ = 'action_history'

    id: Mapped[int] = mapped_column(primary_key=True)
    action_name: Mapped[str] = mapped_column(String(100))
    context: Mapped[dict] = mapped_column(JSON)
    created_at: Mapped[datetime] = mapped_column(DateTime)
