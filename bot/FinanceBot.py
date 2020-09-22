from datetime import datetime
import telebot
from bot import config
from Banks import PrivatValut as pr
from Keyboards import currency_kb
from Banks import mono
import sys

import subprocess

from Keyboards import chosen_currensy_kb as ch_kb
bot = telebot.TeleBot(config.TOKEN)
coast_categories = [100]


@bot.message_handler(commands=['exchange'])
def send_curr(message):
    send_privat_course(message)


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "Приветствую, {0.first_name}. Меня зовут {1.first_name}, "
                                      "я создан, что бы помогать следить за актуальным курсом валют. "
                                      "Надеюсь, я буду полезен.  "
                     .format(message.from_user, bot.get_me()),
                     parse_mode='html')

    bot.send_message(message.chat.id, "Вы хотите, чтобы я отправил вам акутальный курс валют?",
                     reply_markup=currency_kb.markup_send_curr)


@bot.message_handler(content_types=['text'])
def manage_buttons(message):
    if message.text == "Курс валют":
        send_privat_course(message)
    elif message.text == "Да, отправляй":
        send_privat_course(message)
        send_chosen_curr(message)
    elif message.text == "Польский злотый":
        send_zloty(message)


def send_privat_course(message):
    subprocess.Popen([sys.executable, '../Banks/PrivatValut.py'])
    now = datetime.now()
    bot.send_message(message.chat.id, "Курс валют к гривне на " + str(now.day) + "." + str(now.month) +
                     "." + str(now.year) + ":\n\n" + "USD/Доллар: \n" + "покупка " + str(pr.usd_buy)
                     + " продажа " + str(pr.usd_sale) + ":\n\n"
                     + "Euro/Евро: \n" + "покупка " + str(pr.euro_buy) + " продажа "
                     + str(pr.euro_sale) + " UAH" + ":\n\n" + "BTC/Биткоин: \n" + "покупка "
                     + str(pr.btc_buy) + " $" + " продажа " + str(pr.btc_sale) + " $")


def send_chosen_curr(message):
    bot.send_message(message.chat.id, "Вы можете следить за курсом выбраной вами валюты. "
                                      "Какую валюты вы хотите отслеживать? (Курс выбраной вами валюты будет оцениваться"
                                      "монобанком)", reply_markup=ch_kb.markup_chosen_curr)


def send_zloty(message):
    subprocess.Popen([sys.executable, '../Banks/PrivatValut.py'])
    now = datetime.now()
    bot.send_message(message.chat.id, "Курс злотого на " + str(now.day) + "." + str(now.month) + "." +
                     str(now.year) + "." +
                     ":\n\n" + "Zloty/Злотый: \n\n" + "покупка: " + str(mono.zloty_buy) + "продажа: " +
                     str(mono.zloty_sell))


bot.polling(none_stop=True)
