from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from decouple import config


bot = Bot(config('TOKEN'))  # привязка токена
dp = Dispatcher(bot=bot)  # вызываем диспетчер


@dp.message_handler(commands=['start'])  # перехватчик команды старт
async def start_command(message: types.Message):  # асинх функция
    await message.answer(f"Здрасвтсвуйте хозяин, {message.from_user.first_name}, я ваш верный слуга")  # ответ бота


@dp.message_handler(commands=['quiz_1'])  # команда для квиза
async def quiz_1(message: types.Message):
    question = 'Когда был создан Python?'  # вопрос
    #  варианты ответов
    answers = [
        '2000г',
        '1991г',
        '1980г',
        '1995г'
    ]
    await bot.send_poll(
        message.from_user.id,  # кому? мне
        question=question,  # вопрос
        options=answers,  # варианты ответов
        type='quiz',  # тип квиз
        correct_option_id=1,  # правильный вариант ответа
    )


@dp.message_handler(commands='quiz_2')
async def quiz_2(message: types.Message):
    question = 'Сколько языков программирования существует на данный момент?'
    answers = [
        '100',
        '57',
        '10',
        '700+'
    ]

    await bot.send_poll(
        message.from_user.id,
        question=question,
        options=answers,
        correct_option_id=3,
        is_anonymous=False,  # неанонимный опрос
        type='quiz',
        open_period=30,  # ограничения во времени
        explanation='Много)'  # типа подсказка
    )


@dp.message_handler(commands=['meme'])  # для мема
async def show_meme(message: types.Message):
    meme = open('media/meme.jpg', 'rb')  # открываем файл с мемом
    await bot.send_photo(message.from_user.id, photo=meme)  # отправляем наш мем
    meme.close()  # закрываем файл


@dp.message_handler()  # для всех
async def echo(message: types.Message):  # эхо бот
    if message.text.isdigit():  # если число
        await message.answer(int(message.text) ** 2)  # возводим во 2 степень
    else:
        await message.answer(message.text)  # иначе возвращаем как эхо


if __name__ == '__main__':  # точка входа
    executor.start_polling(dp)  # вызываем функцию
