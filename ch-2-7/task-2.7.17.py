from datetime import datetime

from sqlalchemy import DateTime, func, String, Integer, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class AuditStampMixin:
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), server_onupdate=func.now(),
                                                 nullable=False)


class Base(DeclarativeBase):
    pass


class DeliveryShipment(Base, AuditStampMixin):
    __tablename__ = 'delivery_shipments'
    id: Mapped[int] = mapped_column(primary_key=True)
    tracking_code: Mapped[str] = mapped_column(String(32), nullable=False)
    weight_grams: Mapped[int] = mapped_column(Integer, nullable=False)


class ReturnPackage(Base, AuditStampMixin):
    __tablename__ = 'return_packages'
    id: Mapped[int] = mapped_column(primary_key=True)
    rma_code: Mapped[str] = mapped_column(String(24), nullable=False)
    reason_text: Mapped[str | None] = mapped_column(Text, nullable=True)
