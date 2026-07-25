# Создайте модель Category для категорий товаров с именем таблицы в базе данных categories
#
# Поля:
#
# Объявите id как первичный ключ через Mapped[int] и mapped_column(primary_key=True).
# Объявите name как строчное поле через Mapped[str] и mapped_column().

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String


class Base(DeclarativeBase):
    pass

# Напишите ваш код тут
class Category(Base):
    __tablename__ = "categories"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()

