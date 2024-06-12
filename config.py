from dotenv import load_dotenv
import os

from telebot import TeleBot

load_dotenv()
bot = TeleBot(
    os.getenv("BOT_TOKEN")
)  # Токен, полученный от BotFather.