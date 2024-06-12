from telebot.types import ReplyKeyboardRemove
from config import bot
from database.bd import CurrentUser


@bot.message_handler(func=lambda message: message.text == "Выход❌")
def handle_exit(message):
    CurrentUser.CurrentId = 0
    bot.send_message(
        message.from_user.id,
        "Вы вышли из чат-бота",
        reply_markup=ReplyKeyboardRemove()
    )
