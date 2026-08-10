from sqlalchemy import Integer, String, JSON
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class WebhookAudit(Base):
    __tablename__ = 'webhook_audits'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    target_url: Mapped[str] = mapped_column(String(255))
    request_data: Mapped[dict] = mapped_column(JSON)
    response_data: Mapped[dict | None] = mapped_column(JSON, nullable=True)
