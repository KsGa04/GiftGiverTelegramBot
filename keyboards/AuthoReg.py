from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


def gen_markup():
    # Создаём объекты кнопок.
    button_1 = InlineKeyboardButton(text="Авторизация", callback_data="author")
    button_2 = InlineKeyboardButton(text="Регистрация", callback_data="reg")

    # Создаём объект клавиатуры, добавляя в него кнопки.
    keyboard = InlineKeyboardMarkup()
    keyboard.add(button_1, button_2)
    return keyboard