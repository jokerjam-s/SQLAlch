# Создайте ORM-модель Account(Base) с именем таблицы в базе данных accounts. Добавьте поля и атрибуты:
# ORM-поля:
# Объявите account_id как первичный ключ через Mapped[int] и mapped_column(primary_key=True).
# Объявите email как строчное поле через Mapped[str] и mapped_column().
# Обычные атрибуты (не ORM-поля):
# Добавьте атрибут has_access типа bool.
# Добавьте атрибут session_token типа str.
# Требование:
# Сделайте так, чтобы ORM корректно создал модель, и в маппинге (то есть в таблице) присутствовали только поля account_id и email, а has_access и session_token не попадали в ORM-маппинг.

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Account(Base):
    __tablename__ = "accounts"
    __allow_unmapped__ = True

    account_id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column()

    has_access: bool
    session_token: str


