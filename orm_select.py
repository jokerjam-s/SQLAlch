from sqlalchemy import create_engine, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

engine = create_engine("sqlite:///orm_example.db", echo=True)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50))

Base.metadata.create_all(engine)

with Session(engine) as session:
    session.query(User).delete()

    alice = User(name="Alice")
    bob = User(name="Bob")
    charlie = User(name="Charlie")

    session.add_all([alice, bob, charlie])
    session.commit()

from sqlalchemy import select

with Session(engine) as session:
    stmt = select(User)
    print("ORM выражение select:", stmt)
    result = session.execute(stmt)

    for row in result:
        print("Сырая строка результата:", row)

    result = session.execute(stmt)

    users = result.scalars().all()

    for user in users:
        print("id:", user.id, "name:", user.name)