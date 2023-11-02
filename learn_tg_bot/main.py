import telebot
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from config import host, user, password, db_name, port, Users


bot = telebot.TeleBot('token')
url = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db_name}"   #строка подключения к бд
engine = create_engine(url)


@bot.message_handler(commands=['start'])
def start(message):
    session = Session(engine)
    if not session.get(Users, message.chat.id):
        bot.send_message(message.chat.id, 'Привет, сейчас тебя зарегистрируем. Введи свое имя')
        bot.register_next_step_handler(message, user_name)
    else:
        bot.send_message(message.chat.id, 'Привет, ты уже зарегистрирован. Чтобы узнать возможности бота пиши /help')


def user_name(message):
    name = message.text.strip()
    new_user = Users(
        id=message.chat.id,
        f_name=name
    )
    session = Session(bind=engine)
    if not session.get(Users, message.chat.id):
        session.add(new_user)
        session.commit()
    session.close()

bot.polling(none_stop=True)


