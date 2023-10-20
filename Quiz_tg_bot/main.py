import telebot
from telebot import types
import sqlite3


bot = telebot.TeleBot('token') # получаем доступ к боту
quiz_bd_info = list()
question_number = 0
score = 0


@bot.message_handler(commands=['start'])
def start_func(message):
    global score, question_number
    question_number = 0
    score = 0
    message_text = """
    Сегодня ты участвуешь в викторине по информатике\n
    Правила:\n
    1) Когда будешь готов - введи команду <b>/go</b> и викторина начнется\n
    2) После начала бот будет присылать тебе вопросы и возможные варианты ответов в виде кнопок\n
    3) После твоего выбора вводи команду <b>/next</b> чтобы перейти к следующему вопросу\n
    4) Когда закончишь позови преподавателя. Он сообщит тебе команду для получения результатов. Успехов!\n
    Готов?(для старта введи /go)
    """
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}.\n')
    bot.send_message(message.chat.id, message_text, parse_mode='html')


# @bot.message_handler(commands=['go', 'GO', 'Go'])
# def main_body(message):
#     conn = sqlite3.connect('quiz_bd1.sql')
#     cur = conn.cursor()  # создаем объект курсор через который сможем выполнять команды к бд
#     cur.execute('SELECT * FROM Quiz')
#     quiz_bd_info = cur.fetchall()  # вернет все найденные записи из бд
#
#     for info in quiz_bd_info:
#         answers = info[2].split()
#         markup = types.InlineKeyboardMarkup()  # создали объект для добавления inline кнопок
#         btn1 = types.InlineKeyboardButton(answers[0], callback_data='correct') if answers[0] == info[3] else types.InlineKeyboardButton(answers[0], callback_data='wrong')
#         btn2 = types.InlineKeyboardButton(answers[1], callback_data='correct') if answers[1] == info[3] else types.InlineKeyboardButton(answers[1], callback_data='wrong')
#         btn3 = types.InlineKeyboardButton(answers[2], callback_data='correct') if answers[2] == info[3] else types.InlineKeyboardButton(answers[2], callback_data='wrong')
#         btn4 = types.InlineKeyboardButton(answers[3], callback_data='correct') if answers[3] == info[3] else types.InlineKeyboardButton(answers[3], callback_data='wrong')
#         markup.row(btn1, btn2)
#         markup.row(btn3, btn4)
#         bot.send_message(message.chat.id, info[1], reply_markup=markup)
#         func=lambda callback: True
#         if func == 'correct':
#             score += 1
#
#
#     cur.close()
#     conn.close()
#
#
# @bot.callback_query_handler(func=lambda callback: True)
# def callback_reaction(callback):
#     global score
#     if callback == 'correct':
#         score += 1


@bot.message_handler(commands=['go'])
def first_question(message):
    global quiz_bd_info, question_number
    conn = sqlite3.connect('quiz_bd1.sql')
    cur = conn.cursor()  # создаем объект курсор через который сможем выполнять команды к бд
    cur.execute('SELECT * FROM Quiz')
    quiz_bd_info = cur.fetchall()  # вернет все найденные записи из бд
    answers = quiz_bd_info[question_number][2].split()
    markup = types.InlineKeyboardMarkup()  # создали объект для добавления inline кнопок
    btn1 = types.InlineKeyboardButton(answers[0], callback_data='correct') if answers[0].lower() == quiz_bd_info[question_number][3].lower() else types.InlineKeyboardButton(answers[0], callback_data='wrong')
    btn2 = types.InlineKeyboardButton(answers[1], callback_data='correct') if answers[1].lower() == quiz_bd_info[question_number][3].lower() else types.InlineKeyboardButton(answers[1], callback_data='wrong')
    btn3 = types.InlineKeyboardButton(answers[2], callback_data='correct') if answers[2].lower() == quiz_bd_info[question_number][3].lower() else types.InlineKeyboardButton(answers[2], callback_data='wrong')
    btn4 = types.InlineKeyboardButton(answers[3], callback_data='correct') if answers[3].lower() == quiz_bd_info[question_number][3].lower() else types.InlineKeyboardButton(answers[3], callback_data='wrong')
    markup.row(btn1, btn2)
    markup.row(btn3, btn4)
    bot.send_message(message.chat.id, quiz_bd_info[question_number][1], reply_markup=markup)
    question_number += 1

@bot.callback_query_handler(func=lambda callback: True)
def first_question_buttons(callback):
    global score
    if callback.data == 'correct':
        bot.send_message(callback.message.chat.id, 'Ответ принят. Введи /next для получения следующего вопроса')
        score += 1
    else:
        bot.send_message(callback.message.chat.id, 'Ответ принят. Введи /next для получения следующего вопроса')


@bot.message_handler(commands=['next'])
def other_questions(message):
    global quiz_bd_info, question_number
    if question_number > len(quiz_bd_info) -1:
        bot.send_message(message.chat.id, 'Вопросы закончились, зови преподавателя 👍')
    else:
        answers = quiz_bd_info[question_number][2].split()
        markup = types.InlineKeyboardMarkup()  # создали объект для добавления inline кнопок
        btn1 = types.InlineKeyboardButton(answers[0], callback_data='correct') if answers[0].lower() == quiz_bd_info[question_number][3].lower() else types.InlineKeyboardButton(answers[0], callback_data='wrong')
        btn2 = types.InlineKeyboardButton(answers[1], callback_data='correct') if answers[1].lower() == quiz_bd_info[question_number][3].lower() else types.InlineKeyboardButton(answers[1], callback_data='wrong')
        btn3 = types.InlineKeyboardButton(answers[2], callback_data='correct') if answers[2].lower() == quiz_bd_info[question_number][3].lower() else types.InlineKeyboardButton(answers[2], callback_data='wrong')
        btn4 = types.InlineKeyboardButton(answers[3], callback_data='correct') if answers[3].lower() == quiz_bd_info[question_number][3].lower() else types.InlineKeyboardButton(answers[3], callback_data='wrong')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        bot.send_message(message.chat.id, quiz_bd_info[question_number][1], reply_markup=markup)
        question_number += 1


@bot.callback_query_handler(func=lambda callback: True)
def other_question_buttons(callback):
    global score
    if callback.data == 'correct':
        bot.send_message(callback.message.chat.id, 'Ответ принят. Введи /next для получения следующего вопроса')
        score += 1
    else:
        bot.send_message(callback.message.chat.id, 'Ответ принят. Введи /next для получения следующего вопроса')


@bot.message_handler(commands=['result'])
def result(message):
    bot.send_message(message.chat.id, f'Поздравляю, {message.from_user.first_name} {message.from_user.last_name}. Правильных ответов: {score}')


bot.polling(none_stop=True)    # нужно чтобы программа работала постоянно чтобы бот по кд реагировал