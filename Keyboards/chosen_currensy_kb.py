from telebot import types

markup_chosen_curr = types.ReplyKeyboardMarkup(resize_keyboard=True)

send_curr_zloty = types.KeyboardButton("Польский злотый")
no_one_curr = types.KeyboardButton("Я не хочу следить за курсом какой-то определенной валюты")


markup_chosen_curr.add(send_curr_zloty, no_one_curr)
