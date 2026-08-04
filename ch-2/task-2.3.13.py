from datetime import datetime
from decimal import Decimal

from sqlalchemy import String, CHAR, SmallInteger, Numeric, Integer, Boolean, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class ClientAccount(Base):
    __tablename__ = 'client_accounts'

    id: Mapped[int] = mapped_column(primary_key=True)
    contact_email: Mapped[str] = mapped_column(String(255))
    contact_phone: Mapped[str] = mapped_column(String(20), nullable=True)
    region_code: Mapped[str] = mapped_column(CHAR(2))
    years: Mapped[int] = mapped_column(SmallInteger)
    account_balance: Mapped[Decimal] = mapped_column(Numeric(12,2))
    reward_points: Mapped[int] = mapped_column(Integer)
    verified: Mapped[bool] = mapped_column(Boolean)
    registered_at: Mapped[datetime] = mapped_column(DateTime)
