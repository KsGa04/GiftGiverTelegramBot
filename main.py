from telebot.custom_filters import StateFilter
from telebot.handler_backends import StatesGroup, State
from telebot.types import ReplyKeyboardRemove, Message

from config import bot
from keyboards.AuthoReg import gen_markup
from handlers.authorization import author_answer
from handlers.registration import reg_answer
from handlers.exit import handle_exit
from handlers.wishList import handle_wish
from handlers.findGift import handle_find
from handlers.selectionOfGift import handle_selection
from keyboards.MainKeyboards import gen_markup_main
from keyboards.OptionallyKeyboards import gen_markup_optionally


@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(
        message.from_user.id,
        "Добро пожаловать! Я чат-бот веб-сайта Gift/Giver",
        reply_markup=gen_markup(),  # Отправляем клавиатуру.
    )

@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    if call.data == "exit":
        handle_exit(call.message)
    else:
        # Обработка других кнопок
        pass


bot.add_custom_filter(StateFilter(bot))
bot.infinity_polling()
