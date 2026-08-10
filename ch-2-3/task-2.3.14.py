from datetime import datetime, time
from decimal import Decimal

from sqlalchemy import String, Numeric, CHAR, Integer, Boolean, DateTime, TIMESTAMP
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class PurchaseOrder(Base):
    __tablename__ = 'purchase_orders'

    id: Mapped[int] = mapped_column(primary_key=True)
    number: Mapped[str] = mapped_column(String(50))
    grand_total: Mapped[Decimal] = mapped_column(Numeric(12, 2))
    vat_amount: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    promo_discount: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    currency_code: Mapped[str] = mapped_column(CHAR(3))
    lines_count: Mapped[int] = mapped_column(Integer)
    paid: Mapped[bool] = mapped_column(Boolean)
    created_on: Mapped[datetime] = mapped_column(DateTime)
    updated_on: Mapped[time] = mapped_column(TIMESTAMP)