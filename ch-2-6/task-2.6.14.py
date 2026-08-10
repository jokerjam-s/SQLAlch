from datetime import datetime

from sqlalchemy import DateTime, func, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class MessageNote(Base):
    __tablename__ = 'message_notes'
    id: Mapped[int] = mapped_column(primary_key=True)
    headline: Mapped[str] = mapped_column(String(200))
    authored_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, server_default=func.now())