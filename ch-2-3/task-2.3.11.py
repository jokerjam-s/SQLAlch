from sqlalchemy import String, Integer, BigInteger, Float, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class PageMetrics(Base):
    __tablename__ = 'page_metrics'

    id: Mapped[int] = mapped_column(primary_key=True)
    address: Mapped[str] = mapped_column(String(255))
    total_views: Mapped[int] = mapped_column(BigInteger)
    unique_hits: Mapped[int] = mapped_column(BigInteger)
    exit_rate: Mapped[float] = mapped_column(Float)
    average_duration: Mapped[float] = mapped_column(Float)
    public: Mapped[bool] = mapped_column(Boolean)
