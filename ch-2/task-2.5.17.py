from datetime import datetime

from sqlalchemy import String, Integer, DateTime, Index, CheckConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class UserAccount(Base):
    __tablename__ = 'user_accounts'

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(255), unique=True)
    handle: Mapped[str] = mapped_column(String(50))
    age: Mapped[int] = mapped_column(Integer)
    created_at: Mapped[datetime] = mapped_column(DateTime)

    __table_args__ = (
        Index('handle', 'handle'),
        CheckConstraint('age >= 0 AND age <= 120'),
    )


