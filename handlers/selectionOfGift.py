from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, ReplyKeyboardRemove
from config import bot
from database.selectionOfGift import get_gifts
from handlers.authorization import user_data
from keyboards.OptionallyKeyboards import gen_markup_optionally


@bot.message_handler(func=lambda message: message.text == "Подбор подарков🎁")
def handle_selection(message):
    bot.send_message(chat_id=message.from_user.id, text="Какой категории вам необходим подарок?", reply_markup=ReplyKeyboardRemove())
    bot.register_next_step_handler(message, gift_selection)


def gift_selection(message: Message):
    user_data["Какой категории вам необходим подарок?"] = message.text
    bot.send_message(chat_id=message.from_user.id, text="Кому хотите подарить подарок?")
    bot.register_next_step_handler(message, recipient)


def recipient(message: Message):
    user_data["Кому хотите подарить подарок?"] = message.text
    bot.send_message(chat_id=message.from_user.id, text="Какого возраста получатель?")
    bot.register_next_step_handler(message, age)


def age(message: Message):
    """Обработка возраста получателя"""
    user_data['age'] = message.text
    gifts = get_gifts(user_data)
    bot.send_message(message.from_user.id, text="Вот что мне удалось подобрать")
    if gifts:
        for item in gifts.Gifts:
            name, link, image, item_id, price = item
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
        bot.send_message(message.from_user.id, text="Подарки найдены.", reply_markup=gen_markup_optionally())
    else:
        bot.send_message(message.from_user.id, text="Подарки не найдены.", reply_markup=gen_markup_optionally())
