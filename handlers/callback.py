from config import bot
from aiogram import types, Dispatcher


# функция квиза 1
async def quiz_1(call: types.callback_query):
    question = 'Когда был создан Python?'
    answers = [
        '2000г',
        '1991г',
        '1980г',
        '1995г'
    ]
    await bot.send_poll(
        call.message.chat.id,
        question=question,
        options=answers,
        type='quiz',
        correct_option_id=1,
    )


# функция квизa 2
async def quiz_2(call: types.CallbackQuery):
    question = 'Сколько языков программирования существует на данный момент?'
    answers = [
        '100',
        '57',
        '10',
        '700+'
    ]

    await bot.send_poll(
        call.message.chat.id,
        question=question,
        options=answers,
        correct_option_id=3,
        is_anonymous=False,
        type='quiz',
        open_period=30,
        explanation='Много)',
    )


# функция квизa 3
async def quiz_3(call: types.CallbackQuery):
    question = 'Что такое питон?'
    answers = [
        'змея',
        'питон',
        'язык программирования',
        'хз'
    ]

    await bot.send_poll(
        call.message.chat.id,
        question=question,
        options=answers,
        correct_option_id=2,
        is_anonymous=False,
        type='quiz',
        open_period=30
    )


# регистрация функций
def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_1, text='button1')
    dp.register_callback_query_handler(quiz_2, text='button2')
    dp.register_callback_query_handler(quiz_3, text='button3')
