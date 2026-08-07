from sqlalchemy import String, Index
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class AccountUser(Base):
    __tablename__ = 'account_users'

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(255))

    __table_args__ = (
        Index('email', 'email'),
    )