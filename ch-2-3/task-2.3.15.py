from datetime import datetime
from decimal import Decimal

from sqlalchemy import String, Numeric, Boolean, DateTime, SmallInteger, Text, CHAR
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class TransactionPayment(Base):
    __tablename__ = 'transaction_payments'

    id: Mapped[int] = mapped_column(primary_key=True)
    reference: Mapped[str] = mapped_column(String(50))
    total_amount: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    service_fee: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    currency_code: Mapped[str] = mapped_column(CHAR(3))
    pay_method: Mapped[str] = mapped_column(String(50))
    successful: Mapped[bool] = mapped_column(Boolean)
    created_on: Mapped[datetime] = mapped_column(DateTime)
    confirmed_on: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    retry_count: Mapped[int] = mapped_column(SmallInteger)
    note: Mapped[str | None] = mapped_column(Text, nullable=True)

