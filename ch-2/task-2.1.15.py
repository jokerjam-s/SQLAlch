# Создайте базовый класс Base, наследующийся от DeclarativeBase.
# Затем объявите две ORM-модели: Profile и Article, обе наследуются от Base.
# Имена таблиц в базе данных:
# Для модели Profile укажите имя таблицы profiles.
# Для модели Article укажите имя таблицы articles.
# Поля:
# Объявите id как первичный ключ через Mapped[int] и mapped_column(primary_key=True) для обеих моделей.

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


# Напишите ваш код тут
class Profile(Base):
    __tablename__ = "profiles"
    id: Mapped[int] = mapped_column(primary_key=True)


class Article(Base):
    __tablename__ = "articles"
    id: Mapped[int] = mapped_column(primary_key=True)
