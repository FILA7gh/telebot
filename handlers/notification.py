from config import bot
from aiogram import types, Dispatcher
import aioschedule
import asyncio


# функция добавления айди пользователя
async def get_chat_id(message: types.Message):
    global chat_id
    chat_id = []
    chat_id.append(message.from_user.id)
    await message.answer('Се се брат')


# напоминание о Джума намазе
async def go_to_juma():
    for id in chat_id:
        await bot.send_message(id, 'пора на Джума намаз!')


# напоминание о единице
async def put_units():
    for id in chat_id:
        await bot.send_message(id, 'Не забудь положить единицы!')


# функция отправки уведомления каждую пятницу
async def scheduler():
    aioschedule.every().second.do(go_to_juma)
    aioschedule.every(2).seconds.do(put_units)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


# функция регистрации функций
def register_handler_notification(dp: Dispatcher):
    dp.register_message_handler(get_chat_id, lambda x: 'напомни э' in x.text.lower())
