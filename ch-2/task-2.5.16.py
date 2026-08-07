from sqlalchemy import Integer, CheckConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Student(Base):
    __tablename__ = 'students'

    id: Mapped[int] = mapped_column(primary_key=True)
    grade_level: Mapped[int] = mapped_column(Integer)

    __table_args__ = (
        CheckConstraint('grade_level >= 1 AND grade_level <= 11'),
    )