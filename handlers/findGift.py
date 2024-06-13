import random

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, ReplyKeyboardRemove

from config import bot
from database.findProduct import search_gifts
from handlers.authorization import user_data
from keyboards.MainKeyboards import gen_markup_main


@bot.message_handler(func=lambda message: message.text == "Поиск подарка🔍")
def handle_find(message):
    """
        Обработчик команды "Поиск подарка🔍"
        """
    bot.send_message(chat_id=message.from_user.id, text="Введите название подарка", reply_markup=ReplyKeyboardRemove())
    bot.register_next_step_handler(message, handle_search)

def handle_search(message: Message):
    """
    Обработчик ввода пользователем названия подарка
    """
    search_term = message.text
    gifts = search_gifts(search_term)

    if gifts:
        # Выбираем 5 случайных подарков из списка
        random_gifts = random.sample(gifts, min(5, len(gifts)))
        for item in random_gifts:
            name, price, link, image, item_id = item
            price_str = "{:.2f}".format(price)
            price_str = price_str.rstrip("0").rstrip(".")
            item_markup = InlineKeyboardMarkup()
            item_markup.add(InlineKeyboardButton("Добавить в желаемое", callback_data=f"add_item_{item_id}"))

            # Отправка изображения подарка
            if image:
                try:
                    bot.send_photo(message.from_user.id, photo=image,
                                   caption=f'<a href="{link}" style="color:black;text-decoration:none;">{name} (Цена: {price_str})</a>',
                                   parse_mode='HTML', reply_markup=item_markup)
                except Exception as e:
                    print(f"Ошибка при отправке изображения: {e}")
            else:
                bot.send_message(message.from_user.id,
                                 text=f'<a href="{link}" style="color:black;text-decoration:none;">{name} (Цена: {price_str})</a>',
                                 parse_mode='HTML', reply_markup=item_markup)
        bot.send_message(message.from_user.id, text="Подарки найдены.", reply_markup=gen_markup_main())
    else:
        bot.send_message(message.from_user.id, text="Подарки не найдены.", reply_markup=gen_markup_main())

    user_data["state"] = None