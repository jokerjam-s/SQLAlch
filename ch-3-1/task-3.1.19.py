from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class TrainingModule(Base):
    __tablename__ = 'training_modules'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    lessons: Mapped[list['TrainingLesson']] = relationship('TrainingLesson', order_by='TrainingLesson.name')


class TrainingLesson(Base):
    __tablename__ = 'training_lessons'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    module_id: Mapped[int] = mapped_column(ForeignKey('training_modules.id'), nullable=False)
