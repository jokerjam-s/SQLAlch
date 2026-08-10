from decimal import Decimal

from sqlalchemy import Numeric, Integer, Computed
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass

class InvoiceRow(Base):
    __tablename__ = 'invoice_rows'
    id: Mapped[int] = mapped_column(primary_key=True)
    unit_price: Mapped[int] = mapped_column(Integer)
    quantity: Mapped[int] = mapped_column(Integer)
    total_amount: Mapped[int] = mapped_column(Computed("unit_price * quantity"))
