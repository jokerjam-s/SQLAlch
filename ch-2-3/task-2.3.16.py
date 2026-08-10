from datetime import datetime, time, timedelta
from decimal import Decimal

from sqlalchemy import String, CHAR, Numeric, DateTime, Time, Interval, Boolean, Text, Float, Date
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class DeliveryParcel(Base):
    __tablename__ = 'delivery_parcels'

    id: Mapped[int] = mapped_column(primary_key=True)
    tracking_code: Mapped[str] = mapped_column(String(100))
    service_name: Mapped[str] = mapped_column(String(100))
    from_country: Mapped[str] = mapped_column(CHAR(2))
    to_country: Mapped[str] = mapped_column(CHAR(2))
    mass_kg: Mapped[float] = mapped_column(Float)
    shipping_cost: Mapped[Decimal] = mapped_column(Numeric(12, 2))
    sent_on: Mapped[datetime] = mapped_column(Date)
    sent_at: Mapped[time] = mapped_column(Time)
    eta_date: Mapped[datetime] = mapped_column(Date)
    transit_time: Mapped[timedelta] = mapped_column(Interval)
    express: Mapped[bool] = mapped_column(Boolean)
    delivered: Mapped[bool] = mapped_column(Boolean)
    delivered_on: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    note: Mapped[str | None] = mapped_column(Text, nullable=True)
