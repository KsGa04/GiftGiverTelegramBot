from config import bot
from telebot.types import Message
from database.bd import register_user

user_data = {}


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
        "Введите свой логин:",
    )
    bot.register_next_step_handler(callback_query.message, process_login)


def process_login(message: Message):
    user_data["login"] = message.text
    bot.send_message(
        message.from_user.id,
        "Введите свой пароль:",
    )
    bot.register_next_step_handler(message, process_password)


def process_password(message: Message):
    user_data["password"] = message.text
    bot.send_message(
        message.from_user.id,
        "Введите своё ФИО:",
    )
    bot.register_next_step_handler(message, process_fio)


def process_fio(message: Message):
    user_data["fio"] = message.text
    bot.send_message(
        message.from_user.id,
        "Введите свою электронную почту:",
    )
    bot.register_next_step_handler(message, process_email)


def process_email(message: Message):
    user_data["email"] = message.text
    reg_message = register_user(user_data["login"], user_data["password"], user_data["fio"], user_data["email"])
    bot.send_message(
        message.from_user.id,
        reg_message
    )
