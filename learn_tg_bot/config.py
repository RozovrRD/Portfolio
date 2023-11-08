from sqlalchemy import create_engine, Integer, String, Column
from sqlalchemy.orm import declarative_base
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT    # когда файл запускается 1й раз благодаря этим библиотекам происходит
# создание бд (именно бд) в pgAdmin4


host = "localhost"
user = "postgres"
password = ""
db_name = ""
port = ''

# connection = psycopg2.connect(user=user, password=password)   #эти строки создают бд в пгадмин4
# connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT) # это нужно чтобы избежать ошибки во время создания бд (нельзя выполнить создангие бд внутри блока транзакции)
# cursor = connection.cursor()
# sql_create_db = cursor.execute('create database tg_test_db_users')
# cursor.close()
# connection.close()

url = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db_name}"   #строка подключения к бд
engine = create_engine(url)

Base = declarative_base()   #Базовый класс управляет каталогом классов и таблиц.  крч это нужно чтобы создать норм класс-модель таблицы в бд
# Другими словами, декларативный базовый класс — это оболочка над маппером и MetaData.
# Маппер соотносит подкласс с таблицей, а MetaData сохраняет всю информацию о базе данных и ее таблицах.
# По аналогии с Core в ORM методы create_all() и drop_all() объекта MetaData используются для создания и удаления таблиц.


class Users(Base):             #создаем класс-модель таблицы в бд
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    f_name = Column(String(100), nullable=False)
    equ_score = Column(Integer, nullable=False, default=0)


Base.metadata.create_all(engine)   # добавляем в бд все описанные выше таблицы

