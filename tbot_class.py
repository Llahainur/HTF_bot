import setuptools.wheel

from tokens import Tokens as T
import telebot
from classes import Person

T.tg_token

bot = telebot.TeleBot(T.tg_token)

global P
P = Person


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/hello':
        bot.send_message(message.from_user.id,
                         "Вы водитель или пассажир? Если вы водитель напишите слово водитель. Если вы пассажир "
                         "напишите слово пассажир")
        bot.register_next_step_handler(message, who)


def who(message):
    if message.text == 'водитель':
        bot.send_message(message.from_user.id, "Вы водитель")
        # bot.send_message(message.from_user.id, text1)
        P.is_driver = True
        bot.register_next_step_handler(message, name_of_person)
    elif message.text == 'пассажир':
        bot.send_message(message.from_user.id, "Вы пассажир")
        bot.send_message(message.from_user.id, )
        # bot.send_message(message.from_user.id, text1)
        P.is_driver = False
        bot.register_next_step_handler(message, name_of_person)
    else:
        bot.send_message(message.from_user.id, "Ошибка ввода")
        bot.register_next_step_handler(message, start)


def name_of_person(message):
    print('dbg1')
    bot.send_message(message.from_user.id, "Как вас зовут?")
    bot.register_next_step_handler(message, phonenumber)


def phonenumber(message):
    P.name = message.text
    bot.send_message(message.from_user.id, "Напишите ваш номер телефона (опционально, можно оставить пробел)")
    bot.register_next_step_handler(message, from_addr)


def from_addr(message):
    P.phone = message.text
    bot.send_message(message.from_user.id, "Напишите адрес начала маршрута")
    bot.register_next_step_handler(message, to_addr)


def to_addr(message):
    P.addr_arr = message.text
    bot.send_message(message.from_user.id, "Напишите адрес конца маршрута")
    bot.register_next_step_handler(message, wait)


def wait(message):
    P.addr_dest = message.text
    bot.send_message(message.from_user.id,
                     "Ваш адрес начала маршрута" + P.geocode_arr["addr"] + "Ваш адрес конца маршрута" + P.geocode_dest[
                         "addr"])
    bot.send_message(message.from_user.id, "Подождите, подбираем вам попутчиков")


bot.polling(none_stop=True, interval=0)
