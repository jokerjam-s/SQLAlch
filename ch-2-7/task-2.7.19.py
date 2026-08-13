from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, ForeignKey, Integer


class Base(DeclarativeBase):
    pass


class DocEntry(Base):
    __tablename__ = "doc_entries"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(160), nullable=False)
    doc_kind: Mapped[str] = mapped_column(String(20), nullable=False)  # дискриминатор

    __mapper_args__ = {
        "polymorphic_on": doc_kind,
        "polymorphic_identity": "doc",
    }

# Напишите ваш код тут
class InvoiceDoc(DocEntry):
    __tablename__ = "invoice_docs"
    id: Mapped[int] = mapped_column(ForeignKey("doc_entries.id"), primary_key=True)
    invoice_no: Mapped[str] = mapped_column(String(30), nullable=False)
    amount_cents: Mapped[int] = mapped_column(Integer, nullable=False)

    __mapper_args__ = {
        "polymorphic_identity": "invoice",
    }