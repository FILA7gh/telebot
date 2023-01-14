from datetime import date
from config import bot, ADMINS
from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.client_kb import start_markup
from time import sleep


# функция старта
async def start_command(message: types.Message):
    # для админов
    if message.from_user.id in ADMINS:
        await bot.send_message(message.chat.id,
                               f" Здравcтвуйте хозяин {message.from_user.first_name},"
                               f" я ваш верный слуга", reply_markup=start_markup)
    # для участников
    else:
        await bot.send_message(message.chat.id, f"Привет {message.from_user.first_name}, я ваш помощник)")


# функция кнопок квизов
async def quiz(message: types.Message):

    markup = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton('quiz1', callback_data='button1')
    button2 = InlineKeyboardButton('quiz2', callback_data='button2')
    button3 = InlineKeyboardButton('quiz3', callback_data='button3')
    markup.add(button1, button2, button3)

    await bot.send_message(message.chat.id, 'Выберите квиз:', reply_markup=markup)


# функция мема
async def show_meme(message: types.Message):
    meme = open('media/meme.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=meme)
    meme.close()


# функция даты
async def show_date(message: types.Message):
    await message.answer(f'Текущая дата: {date.today()}')


# функция боли
async def know_the_pain(message: types.Message):
    pain = open('media/pain.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=pain)
    await message.answer(f'{message.from_user.first_name} вы познали боль!')
    pain.close()


# игра для бота с участником
async def dice(message: types.Message):

    await bot.send_message(message.chat.id, 'Мой')
    player_bot = await bot.send_dice(message.chat.id)
    await bot.send_message(message.chat.id, 'Твой')
    player1 = await bot.send_dice(message.chat.id)

    # определение победителя
    sleep(4)
    if player_bot.dice.value > player1.dice.value:
        await bot.send_message(message.chat.id, 'я выиграл!')
    elif player_bot.dice.value < player1.dice.value:
        await bot.send_message(message.chat.id, 'ты выиграл!')
    else:
        await bot.send_message(message.chat.id, 'ничья!')


# регистрация функций
def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(quiz, commands=['quiz'])
    dp.register_message_handler(show_meme, commands=['meme'])
    dp.register_message_handler(show_date, commands=['date'])
    dp.register_message_handler(know_the_pain, commands=['pain'])
    dp.register_message_handler(dice, commands=['dice'])
