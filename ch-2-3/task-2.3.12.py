from sqlalchemy import String, Text, CHAR, Integer, Float, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class BlogEntry(Base):
    __tablename__ = 'blog_entries'

    id: Mapped[int] = mapped_column(primary_key=True)
    headline: Mapped[str] = mapped_column(String(150))
    teaser: Mapped[str | None] = mapped_column(String(255), nullable=True)
    body: Mapped[str] = mapped_column(Text)
    lang: Mapped[str] = mapped_column(CHAR(2))
    view_count: Mapped[int] = mapped_column(Integer)
    score: Mapped[float] = mapped_column(Float)
    published: Mapped[bool] = mapped_column(Boolean)