from decimal import Decimal

from sqlalchemy import String, Numeric, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class InventoryItem(Base):
    __tablename__ = 'inventory_items'

    id: Mapped[int] = mapped_column(primary_key=True)
    label: Mapped[str] = mapped_column(String(200))
    unit_cost: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    stock: Mapped[int] = mapped_column(Integer)
    available: Mapped[bool] = mapped_column()
    
