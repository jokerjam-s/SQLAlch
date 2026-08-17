from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, DeclarativeBase, mapped_column


class Base(DeclarativeBase):
    pass

class DistributionHub(Base):
    __tablename__ = 'distribution_hubs'

    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[str] = mapped_column(String(20), nullable=False, unique=True)


class PalletUnit(Base):
    __tablename__ = 'pallet_units'

    id: Mapped[int] = mapped_column(primary_key=True)
    tag: Mapped[str] = mapped_column(String(30), nullable=False)
    hub_id: Mapped[int] = mapped_column(ForeignKey('distribution_hubs.id'), nullable=False)
    hub: Mapped[list['DistributionHub']] = relationship()