from telebot.types import KeyboardButton, ReplyKeyboardMarkup


def gen_markup_optionally():
    # Создаём объекты кнопок.
    button_1 = KeyboardButton(text="Назад⬅️")
    button_2 = KeyboardButton(text="Ещё➡️")

    # Создаём объект клавиатуры, добавляя в него кнопки.
    keyboard = ReplyKeyboardMarkup(
        row_width=2,
        resize_keyboard=True,  # Автоматически подстраивает размер кнопок
    )
    keyboard.add(button_1, button_2)
    return keyboard