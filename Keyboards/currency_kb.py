from telebot import types

markup_send_curr = types.ReplyKeyboardMarkup(resize_keyboard=True)

send_curr_yes = types.KeyboardButton("Да, отправляй")
send_curr_no = types.KeyboardButton("Нет, спасибо")

markup_send_curr.add(send_curr_yes, send_curr_no)
