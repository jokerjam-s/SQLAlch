from sqlalchemy import Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Registration(Base):
    __tablename__ = 'registrations'

    student_ref: Mapped[int] = mapped_column(primary_key=True)
    course_ref: Mapped[int] = mapped_column(primary_key=True)
    score: Mapped[int] = mapped_column(Integer)
