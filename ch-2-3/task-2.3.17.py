from datetime import date, datetime

from sqlalchemy import Integer, String, BigInteger, Float, Date, DateTime, Boolean, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class InsightReport(Base):
    __tablename__ = 'insight_reports'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    headline: Mapped[str] = mapped_column(String(200))
    view_total: Mapped[int] = mapped_column(BigInteger)
    unique_view_total: Mapped[int] = mapped_column(BigInteger)
    likes_count: Mapped[int] = mapped_column(Integer)
    dislikes_count: Mapped[int] = mapped_column(Integer)
    score: Mapped[float] = mapped_column(Float)
    conversion_pct: Mapped[float] = mapped_column(Float)
    report_on: Mapped[date] = mapped_column(Date)
    generated_on: Mapped[datetime] = mapped_column(DateTime)
    public: Mapped[bool] = mapped_column(Boolean)
    archived: Mapped[bool] = mapped_column(Boolean)
    owner_name: Mapped[str] = mapped_column(String(100))
    unit_name: Mapped[str] = mapped_column(String(100))
    abstract: Mapped[str] = mapped_column(Text)
    internal_notes: Mapped[str | None] = mapped_column(Text, nullable=True)
