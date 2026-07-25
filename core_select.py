from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, Column, Integer, String

# Создаём Engine для SQLite, база будет храниться в файле example.db
engine = create_engine("sqlite:///example.db", echo=True)

# Контейнер для описаний таблиц
metadata = MetaData()

# Описание таблицы users
users = Table(
    "users",  # имя таблицы в базе
    metadata,  # объект MetaData, к которому привязана таблица
    Column("id", Integer, primary_key=True),  # целочисленный первичный ключ
    Column("name", String(50)),  # строковая колонка длиной до 50 символов
)

# Создаём таблицы в базе по описанию в metadata
metadata.create_all(engine)

from sqlalchemy import text

# Вставим тестовые данные
with engine.begin() as conn:
    # Очистим таблицу, если пример запускается повторно
    conn.execute(text("DELETE FROM users"))

    # Вставим несколько пользователей
    conn.execute(
        text("INSERT INTO users (name) VALUES (:name)"),
        {"name": "Alice"},
    )
    conn.execute(
        text("INSERT INTO users (name) VALUES (:name)"),
        {"name": "Bob"},
    )
    conn.execute(
        text("INSERT INTO users (name) VALUES (:name)"),
        {"name": "Charlie"},
    )

from sqlalchemy import select

# Создаём объект запроса: выбрать все колонки таблицы users
stmt = select(users)
print("Выражение select:", stmt)
# Выполняем запрос и печатаем строки
with engine.connect() as conn:
    result = conn.execute(stmt)

    print("\nРезультат SELECT:")
    for row in result:
        print("Строка результата:", row)

print("\nДоступ к полям по имени:")
with engine.connect() as conn:
    result = conn.execute(stmt)

    for row in result:
        print("id:", row.id, "name:", row.name)

print("\nSELECT внутри транзакции engine.begin():")
with engine.begin() as conn:
    result = conn.execute(stmt)
    for row in result:
        print(row.id, row.name)
