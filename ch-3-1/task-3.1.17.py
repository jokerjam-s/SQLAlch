from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column, DeclarativeBase


class Base(DeclarativeBase):
    pass


class UserProfile(Base):
    __tablename__ = 'user_profiles'

    id: Mapped[int] = mapped_column(primary_key=True)
    display_name: Mapped[str] = mapped_column(String(120), nullable=False)
    credential: Mapped['CredentialCard'] = relationship('CredentialCard', back_populates='profile', uselist=False)


class CredentialCard(Base):
    __tablename__ = 'credential_cards'

    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[str] = mapped_column(String(20), nullable=False, unique=True)
    profile_id: Mapped[int] = mapped_column(ForeignKey('user_profiles.id'), nullable=False, unique=True)
    profile: Mapped[list['UserProfile']] = relationship('UserProfile', back_populates='credential')
