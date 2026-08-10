from sqlalchemy import Integer, String, UniqueConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class ContactEmail(Base):
    __tablename__ = 'contact_emails'

    id: Mapped[int] = mapped_column(primary_key=True)
    account_id: Mapped[int] = mapped_column(Integer)
    email_address: Mapped[str] = mapped_column(String(255))

    __table_args__ = (
        UniqueConstraint('account_id', 'email_address'),
    )