from sqlalchemy import String, ForeignKey, Integer
from sqlalchemy.orm import relationship, Mapped, mapped_column, DeclarativeBase


class Base(DeclarativeBase):
    pass


class AccountUser(Base):
    __tablename__ = 'account_users'
    id: Mapped[int] = mapped_column(primary_key=True)
    login: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    drafts: Mapped[list['NoteDraft']] = relationship('NoteDraft', back_populates='owner')

class NoteDraft(Base):
    __tablename__ = 'note_drafts'

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(String(500), nullable=False)
    owner_id: Mapped[int | None] = mapped_column(Integer, ForeignKey('account_users.id'), nullable=True)
    owner: Mapped[list['AccountUser']] = relationship('AccountUser', back_populates='drafts')
