from sqlalchemy import Integer, PrimaryKeyConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class LineItem(Base):
    __tablename__ = 'line_items'

    order_ref: Mapped[int] = mapped_column(Integer)
    product_ref: Mapped[int] = mapped_column(Integer)
    qty: Mapped[int] = mapped_column(Integer)

    __table_args__ = (
        PrimaryKeyConstraint('order_ref', 'product_ref'),
    )