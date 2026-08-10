from datetime import datetime, UTC

from sqlalchemy import Integer, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


def get_now() -> datetime:
    return datetime.now(UTC)


class Base(DeclarativeBase):
    pass


class UserSignup(Base):
    __tablename__ = "user_signups"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    registered_at: Mapped[datetime] = mapped_column(DateTime, default=get_now)
