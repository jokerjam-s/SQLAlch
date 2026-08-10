from sqlalchemy import create_engine, text
from sqlalchemy.orm import DeclarativeBase, Mapped
from sqlalchemy.testing.schema import mapped_column


class Base(DeclarativeBase):
    pass


class AccountUser(Base):
    __tablename__ = "users"
    __table_args__ = {"schema": "account"}

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True)


engine = create_engine("postgresql+psycopg://postgres:@PostgreSQL-18:5432/stepik_db")
with engine.begin() as conn:
    conn.execute(text("CREATE SCHEMA IF NOT EXISTS account"))

Base.metadata.create_all(engine)

key = AccountUser.__table__.key
full_name = Base.metadata.tables[key].fullname
print(full_name)