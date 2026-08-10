from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


metadata = MetaData(
    naming_convention={
        "pk": "pk_%(table_name)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
    }
)


class Base(DeclarativeBase):
    metadata = metadata


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True)


engine = create_engine("sqlite:///:memory:")
Base.metadata.create_all(engine)

table = Base.metadata.tables["users"]

print("Primary key name:", table.primary_key.name)

for constraint in table.constraints:
    print("Constraint:", constraint.name)