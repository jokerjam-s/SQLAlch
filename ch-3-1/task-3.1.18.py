from decimal import Decimal

from sqlalchemy import String, Numeric, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column, DeclarativeBase


class Base(DeclarativeBase):
    pass

class ProductCard(Base):
    __tablename__ = 'product_cards'

    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[str] = mapped_column(String(32), nullable=False, unique=True)
    prices: Mapped[list['CostRow']] = relationship()
    prices_ro: Mapped[list['CostRow']] = relationship('CostRow', viewonly=True)


class CostRow(Base):
    __tablename__ = 'cost_rows'

    id: Mapped[int] = mapped_column(primary_key=True)
    amount: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    product_id: Mapped[int] = mapped_column(ForeignKey('product_cards.id'), nullable=False)
