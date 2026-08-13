from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.declarative import AbstractConcreteBase
from sqlalchemy import String, Integer

class Base(DeclarativeBase):
    pass

class ActionRecord(AbstractConcreteBase, Base):
    strict_attrs = True

    id: Mapped[int] = mapped_column(primary_key=True)
    cost_units: Mapped[int] = mapped_column(Integer, nullable=False)
    action_kind: Mapped[str] = mapped_column(String(20), nullable=False)


# Напишите ваш код тут
class ExportAction(ActionRecord):
    __tablename__ = "export_actions"

    file_key: Mapped[str] = mapped_column(String(80), nullable=False)
    format_code: Mapped[str] = mapped_column(String(10), nullable=False)

    __mapper_args__ = {
        "polymorphic_identity": "export",
        "concrete": True,
    }


class NotifyAction(ActionRecord):
    __tablename__ = "notify_actions"

    recipient_ref: Mapped[str] = mapped_column(String(60), nullable=False)
    channel_code: Mapped[str] = mapped_column(String(15), nullable=False)

    __mapper_args__ = {
        "polymorphic_identity": "notify",
        "concrete": True,
    }