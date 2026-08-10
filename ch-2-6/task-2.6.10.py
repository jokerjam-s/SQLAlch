from sqlalchemy import String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class ContentDraft(Base):
    __tablename__ = 'content_drafts'

    id: Mapped[int] = mapped_column(primary_key=True)
    status: Mapped[str] = mapped_column(String(24), default="draft")
    body: Mapped[str | None] = mapped_column(Text, nullable=True)