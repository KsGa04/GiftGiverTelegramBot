from telebot.types import KeyboardButton, ReplyKeyboardMarkup


def gen_markup_main():
    # Создаём объекты кнопок.
    button_1 = KeyboardButton(text="Поиск подарка🔍")
    button_2 = KeyboardButton(text="Подбор подарков🎁")
    button_3 = KeyboardButton(text="Список желаемого📜")
    button_4 = KeyboardButton(text="Выход❌")

    # Создаём объект клавиатуры, добавляя в него кнопки.
    keyboard = ReplyKeyboardMarkup(
        row_width=2,
        resize_keyboard=True,  # Автоматически подстраивает размер кнопок
    )
    keyboard.add(button_1, button_2, button_3, button_4)
    return keyboard