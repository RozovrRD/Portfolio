import telebot
from telebot import types
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from config import host, user, password, db_name, port, Users
import requests
import json


bot = telebot.TeleBot('')
url = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db_name}"   #строка подключения к бд
engine = create_engine(url)
API_Weather_key = ''


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
    bot.send_message(message.chat.id, 'Регистрация прошла успешно. Чтобы узнать возможности бота пиши /help')



@bot.message_handler(commands=['help'])
def help_info(message):
    bot.send_message(message.chat.id, '/site выведет список основных сайтов и можно будет на них перейти')
    bot.send_message(message.chat.id, '/alarm напоминалка, которая предупредит тебя о запланированном деле заранее')
    bot.send_message(message.chat.id, '/lifenumber посчитает ваше число жизни по дате рождения')
    bot.send_message(message.chat.id, '/weather выведет погоду в указанном городе')



@bot.message_handler(commands=['site'])
def site_link(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Перейти на сайт google.com', url='https://google.com')
    btn2 = types.InlineKeyboardButton('Перейти на сайт stepik.org', url='https://stepik.org/')
    btn3 = types.InlineKeyboardButton('Перейти на сайт github.com', url='https://github.com/')
    markup.row(btn1)
    markup.row(btn2, btn3)
    bot.send_message(message.chat.id, 'Чтобы перейти на сайт нажми на соответствующую кнопку', reply_markup=markup)


@bot.message_handler(commands=['weather'])
def sity_taker(message):
    city_name = bot.send_message(message.chat.id, 'Напиши название населенного пункта, в котором хочешь узнать погоду')
    bot.register_next_step_handler(city_name, get_weather)


def get_weather(massage):
    city = massage.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&lang=ru&appid={API_Weather_key}&units=metric')
    data = json.loads(res.text)
    #bot.reply_to(massage, f'Сейчас погода: {data["main"]["temp"]}')
    bot.reply_to(massage, f'{data["name"]}: {data["weather"][0]["description"]}, за окном {data["main"]["temp"]} градуса')



bot.polling(none_stop=True)