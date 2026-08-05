from datetime import date, datetime
from decimal import Decimal

from sqlalchemy import DateTime, BigInteger, Integer, Float, Numeric, CHAR, String, Boolean, Text, Date
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class MetricSnapshot(Base):
    __tablename__ = 'metric_snapshots'

    id: Mapped[int] = mapped_column(primary_key=True)
    report_date: Mapped[date] = mapped_column(Date)
    generated_at: Mapped[datetime] = mapped_column(DateTime)
    total_users: Mapped[int] = mapped_column(BigInteger)
    engaged_users: Mapped[int] = mapped_column(BigInteger)
    first_time_users: Mapped[int] = mapped_column(Integer)
    session_total: Mapped[int] = mapped_column(BigInteger)
    bounce_pct: Mapped[float] = mapped_column(Float)
    avg_session_seconds: Mapped[float] = mapped_column(Float)
    gross_revenue: Mapped[Decimal] = mapped_column(Numeric(10,2))
    orders_total: Mapped[int] = mapped_column(Integer)
    conversion_pct: Mapped[float] = mapped_column(Float)
    region_code: Mapped[str] = mapped_column(CHAR(2))
    device_category: Mapped[str] = mapped_column(String(50))
    app_platform: Mapped[str] = mapped_column(String(50))
    finalized: Mapped[bool] = mapped_column(Boolean)
    note: Mapped[str | None] = mapped_column(Text, nullable=True)
