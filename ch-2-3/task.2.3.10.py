from sqlalchemy import String, Integer, SmallInteger, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class StockRecord(Base):
    __tablename__ = 'stock_records'

    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[str] = mapped_column(String(50))
    on_hand: Mapped[int] = mapped_column(Integer)
    allocated: Mapped[int] = mapped_column(Integer)
    reorder_point: Mapped[int] = mapped_column(SmallInteger)
    active: Mapped[bool] = mapped_column(Boolean)