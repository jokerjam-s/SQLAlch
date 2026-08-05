from datetime import date, datetime
from decimal import Decimal

from sqlalchemy import Date, DateTime, BigInteger, Integer, Float, CHAR, String, Boolean, Text, Numeric
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class TrafficSnapshot(Base):
    __tablename__ = 'traffic_snapshots'

    id: Mapped[int] = mapped_column(primary_key=True)
    captured_on: Mapped[date] = mapped_column(Date)
    created_at: Mapped[datetime] = mapped_column(DateTime)
    user_total: Mapped[int] = mapped_column(BigInteger)
    user_active: Mapped[int] = mapped_column(BigInteger)
    user_new: Mapped[int] = mapped_column(Integer)
    session_total: Mapped[int] = mapped_column(BigInteger)
    bounce_pct: Mapped[float] = mapped_column(Float)
    avg_session_time: Mapped[float] = mapped_column(Float)
    revenue_total: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    orders_total: Mapped[int] = mapped_column(Integer)
    conversion_pct: Mapped[float] = mapped_column(Float)
    country_iso: Mapped[str] = mapped_column(CHAR(2))
    device_segment: Mapped[str] = mapped_column(String(50))
    platform_name: Mapped[str] = mapped_column(String(50))
    finalized: Mapped[bool] = mapped_column(Boolean)
    note: Mapped[str | None] = mapped_column(Text, nullable=True)
