from datetime import datetime

from sqlalchemy import Integer, DateTime, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class AuditLedger(Base):
    __tablename__ = 'audit_ledgers'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    logged_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    