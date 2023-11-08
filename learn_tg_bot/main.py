import telebot
from telebot import types
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from config import host, user, password, db_name, port, Users
import requests
import json
from equ_generator import print_equation


bot = telebot.TeleBot('')
url = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db_name}"   #строка подключения к бд
engine = create_engine(url)
API_Weather_key = ''
special_numbers = [11, 22, 33, 44, 55]


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
    bot.send_message(message.chat.id, '/math выдает квадратное уравнение для разминки. В боте ведется статистика решенных уравнений')
    bot.send_message(message.chat.id, '/mathresult выведет количество решенных уравнений')



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
    try:
        city = massage.text.strip().lower()
        res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&lang=ru&appid={API_Weather_key}&units=metric')
        data = json.loads(res.text)
        bot.reply_to(massage, f'{data["name"]}: {data["weather"][0]["description"]}, за окном {data["main"]["temp"]} градуса')
    except Exception:
        bot.send_message(massage.chat.id, 'Ошибка в названии или такого населенного пункта нет в базе данных')


@bot.message_handler(commands=['lifenumber'])
def life_number(message):
    birthday = bot.send_message(message.chat.id, 'Напиши дату своего рождения в формате: дд:мм:гггг, (например 01.01.1990)')
    bot.register_next_step_handler(birthday, get_life_number)


def get_life_number(message):
    try:
        day, month, year = [int(item) for item in message.text.strip().split('.')]
        if day > 31 or month > 12:
            bot.reply_to(message, 'ошибка при вводе даты, воспользуйтесь /lifenumber еще раз')
        else:
            birth_date = message.text.strip().replace('.', '')
            number_of_life = 0
            sum_number = 0
            for num in birth_date:
                number_of_life += int(num)
            buff = number_of_life
            while True:
                sum_number += number_of_life % 10
                number_of_life = number_of_life // 10
                if number_of_life == 0:
                    number_of_life = sum_number
                    sum_number = 0
                if len(str(number_of_life)) == 1 and sum_number == 0:
                    break
            if buff in special_numbers:
                answer_str = 'Твое число жизни: ' + str(buff) + '/' + str(number_of_life)
                bot.reply_to(message, answer_str)
            else:
                answer_str = 'Твое число жизни: ' + str(number_of_life)
                bot.reply_to(message, answer_str)
    except Exception:
        bot.send_message(message.chat.id, 'Ошибка при вводе даты')


@bot.message_handler(commands=['math'])
def equ_creator(message):
    equation, x1, x2 = print_equation()
    solution = [x1, x2]
    bot.send_message(message.chat.id, 'Реши уравнение. Ответным сообщением напиши корни через пробел\n'
                                      'Если корни совпали - то напиши только один.')
    roots = bot.send_message(message.chat.id, equation)
    bot.register_next_step_handler(roots, correct_solution, solution)


def correct_solution(message, solution):
    try:
        roots = [int(item) for item in message.text.strip().split()]
        if set(roots) == set(solution):
            session = Session(bind=engine)
            score = session.get(Users, message.chat.id)
            score.equ_score += 1
            session.add(score)
            session.commit()
            session.close()
            bot.send_message(message.chat.id, 'Верно. Количество решенных уравнений увеличено')
        else:
            bot.send_message(message.chat.id, 'Неверно. Данное уравнение создано случайно. Повторно решить его не получится.\n'
                                              'Но можно запросить у бота новое. Для этого используй коману /math')
    except Exception:
        bot.send_message(message.chat.id, 'Неверно введены ответы. Воспользуйтесь функцией /math чтобы получить новое уравнение')


@bot.message_handler(commands=['mathresult'])
def correct_solution_count(message):
    session = Session(bind=engine)
    current_user = session.get(Users, message.chat.id)
    answer_str = 'Количество решенных вами уравнений - ' + str(current_user.equ_score)
    bot.send_message(message.chat.id, answer_str)


bot.polling(none_stop=True)