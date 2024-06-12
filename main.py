from config import bot
from keyboards.AuthoReg import gen_markup
from handlers.authorization import author_answer


@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(
        message.from_user.id,
        "Добро пожаловать! Я чат-бот веб-сайта Gift/Giver",
        reply_markup=gen_markup(),  # Отправляем клавиатуру.
    )


bot.infinity_polling()


@bot.callback_query_handler(
    func=lambda callback_query: (
            callback_query.data  # Обращаемся к callback_data, указанной при создании кнопки.
            == "reg"
    )
)
def reg_answer(callback_query):
    # Удаляем клавиатуру.
    bot.edit_message_reply_markup(
        callback_query.from_user.id, callback_query.message.message_id
    )
    # Отправляем сообщение пользователю.
    bot.send_message(
        callback_query.from_user.id,
        "Я тоже люблю кошек, они так умилительно мурлыкают!",
    )
