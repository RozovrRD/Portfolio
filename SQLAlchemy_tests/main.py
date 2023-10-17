from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String

# строка подключения
sqlite_database = "sqlite:///metanit.db"

# создаем движок SqlAlchemy
engine = create_engine(sqlite_database, echo=True)


class Base(DeclarativeBase): pass

# создаем модель, объекты которой будут храниться в бд
class Person(Base):
    __tablename__ = "people"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)


# создаем таблицы
Base.metadata.create_all(bind=engine)

# создаем сессию подключения к бд
with Session(autoflush=False, bind=engine) as db:
    # создаем объект Person для добавления в бд
    tom = Person(name="Tom", age=38)
    db.add(tom)  # добавляем в бд
    db.commit()  # сохраняем изменения
    print(tom.id)  # можно получить установленный id
    alice = Person(name="Alice", age=33)
    kate = Person(name="Kate", age=28)
    db.add_all([alice, kate])
    db.commit()
    people = db.query(Person).all()
    for p in people:
        print(f"{p.id}.{p.name} ({p.age})")