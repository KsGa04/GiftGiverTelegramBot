from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import bot
from database.bd import CurrentUser
from database.wishList import get_user_wishlist, delete_from_wishlist


@bot.message_handler(func=lambda message: message.text == "Список желаемого📜")
def handle_wish(message):
    wishlist = get_user_wishlist(CurrentUser.CurrentId)

    if wishlist:
        for item in wishlist:
            name, price, link, item_id, image = item
            price_str = "{:.2f}".format(price)
            price_str = price_str.rstrip("0").rstrip(".")
            item_markup = InlineKeyboardMarkup()
            item_markup.add(InlineKeyboardButton("Удалить", callback_data=f"delete_item_{item_id}"))

            # Отправка изображения подарка
            if image:
                try:
                    bot.send_photo(chat_id=message.from_user.id, photo=image,
                                   caption=f'<a href="{link}" style="color:black;text-decoration:none;">{name} (Цена: {price_str})</a>',
                                   parse_mode='HTML', reply_markup=item_markup)
                except Exception as e:
                    print(f"Ошибка при отправке изображения: {e}")
            else:
                bot.send_message(message.from_user.id,
                                 text=f'<a href="{link}" style="color:black;text-decoration:none;">{name} (Цена: {price_str})</a>',
                                 parse_mode='HTML', reply_markup=item_markup)
    else:
        bot.send_message(message.from_user.id, text="Не удалось получить ваш список желаемого.")


@bot.callback_query_handler(func=lambda call: call.data.startswith("delete_item_"))
def handle_delete_item(call):
    item_id = int(call.data.split("_")[-1])
    if delete_from_wishlist(CurrentUser.CurrentId, item_id):
        bot.answer_callback_query(call.id, "Подарок удален из списка желаемого.")
        # Обновляем список желаемого
        handle_wish(call.message)
    else:
        bot.answer_callback_query(call.id, "Не удалось удалить подарок из списка желаемого.")
