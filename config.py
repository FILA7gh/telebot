from aiogram import Dispatcher, Bot
from decouple import config

bot = Bot(config('TOKEN'))  # привязка токена
dp = Dispatcher(bot=bot)

ADMINS = (2081434201, 819212459)  # айди админов
