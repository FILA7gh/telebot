from aiogram import Dispatcher, Bot
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()  # создаем кэш
bot = Bot(config('TOKEN'))  # привязка токена
dp = Dispatcher(bot=bot, storage=storage)

ADMINS = (2081434201, 819212459)  # айди админов
