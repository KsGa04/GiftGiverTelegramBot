from config import bot
from telebot.types import Message
from database.authorization import authenticate_user
from keyboards.AuthoReg import gen_markup
from keyboards.MainKeyboards import gen_markup_main
from handlers.exit import handle_exit

user_data = {}


@bot.callback_query_handler(
    func=lambda callback_query: (
            callback_query.data  # Обращаемся к callback_data, указанной при создании кнопки.
            == "author"
    )
)
def author_answer(callback_query):
    # Удаляем клавиатуру.
    bot.edit_message_reply_markup(
        callback_query.from_user.id, callback_query.message.message_id
    )
    # Отправляем сообщение пользователю.
    bot.send_message(
        callback_query.from_user.id,
        "Введите свой логин и пароль для авторизации.",
    )
    bot.register_next_step_handler(callback_query.message, process_login_password)


def process_login_password(message: Message):
    # Получаем введенные пользователем данные
    login = message.text.split()[0]
    password = message.text.split()[1]

    result = authenticate_user(login, password)
    if result is True:
        bot.send_message(
            message.from_user.id,
            f"Авторизация прошла успешна",
            reply_markup=gen_markup_main()

        )
    else:
        bot.send_message(
            message.from_user.id,
            f"Данные неверные",
            reply_markup=gen_markup()
        )
