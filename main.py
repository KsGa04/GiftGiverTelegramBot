from telebot.types import ReplyKeyboardRemove, Message

from config import bot
from keyboards.AuthoReg import gen_markup
from handlers.authorization import author_answer
from handlers.registration import reg_answer
from handlers.exit import handle_exit
from handlers.wishList import handle_wish
from handlers.findGift import handle_find
from keyboards.MainKeyboards import gen_markup_main


@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(
        message.from_user.id,
        "Добро пожаловать! Я чат-бот веб-сайта Gift/Giver",
        reply_markup=gen_markup(),  # Отправляем клавиатуру.
    )


bot.infinity_polling()
