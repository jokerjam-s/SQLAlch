from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Text

class Base(DeclarativeBase):
    pass

class Ticket(Base):
    __tablename__ = "tickets"

    id: Mapped[int] = mapped_column(primary_key=True)
    subject: Mapped[str] = mapped_column(String(150), nullable=False)
    channel: Mapped[str] = mapped_column(String(20), nullable=False)  # дискриминатор

    __mapper_args__ = {
        "polymorphic_on": channel,
        "polymorphic_identity": "ticket",
    }


# Напишите ваш код тут
class EmailTicket(Ticket):
    from_addr: Mapped[str | None] = mapped_column(String(255), nullable=True)

    __mapper_args__ = {
        "polymorphic_identity": "email",
    }
