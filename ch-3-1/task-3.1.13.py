from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class CommunityMember(Base):
    __tablename__ = 'community_members'

    id: Mapped[int] = mapped_column(primary_key=True)
    handle: Mapped[str] = mapped_column(String(40), nullable=False, unique=True)
    posts: Mapped[list['CommunityPost']] = relationship()


class CommunityPost(Base):
    __tablename__ = 'community_posts'

    id: Mapped[int] = mapped_column(primary_key=True)
    headline: Mapped[str] = mapped_column(String(120), nullable=False)
    member_id: Mapped[int] = mapped_column(ForeignKey('community_members.id'), nullable=False)
