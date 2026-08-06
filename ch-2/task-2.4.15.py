from enum import Enum

from sqlalchemy import Integer, Enum as SAEnum, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class ShippingState(Enum):
    CREATED = 'CREATED'
    IN_TRANSIT = 'IN_TRANSIT'
    DELIVERED = 'DELIVERED'


class Base(DeclarativeBase):
    pass


class DeliveryPackage(Base):
    __tablename__ = 'delivery_packages'

    id :Mapped[int] = mapped_column(Integer, primary_key=True)
    state : Mapped[ShippingState] = mapped_column(SAEnum(ShippingState))
    is_express : Mapped[bool] = mapped_column(Boolean)
