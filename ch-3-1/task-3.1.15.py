from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column, DeclarativeBase


class Base(DeclarativeBase):
    pass


class Collection(Base):
    __tablename__ = 'collections'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(80), nullable=False)
    items: Mapped[list['CollectionItem']] = relationship('CollectionItem', back_populates='collection')


class CollectionItem(Base):
    __tablename__ = 'collection_items'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    collection_id: Mapped[int] = mapped_column(ForeignKey('collections.id'), nullable=False)
    collection: Mapped[list] = relationship('Collection', back_populates='items')
