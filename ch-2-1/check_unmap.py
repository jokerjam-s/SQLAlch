from sqlalchemy.orm import Mapped, DeclarativeBase

class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user"
    __allow_unmapped__ = True

    id: Mapped[int]
    name: Mapped[str]

    is_admin: bool
    cache_key = "user"


