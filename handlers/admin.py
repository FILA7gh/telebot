import random
from config import ADMINS, bot
from aiogram import types, Dispatcher
from database.painbot_db import sql_random, sql_delete, sql_all
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


# функция бана участника по отметке
async def ban(message: types.Message):
    if message.chat.type != 'private':
        if message.from_user.id not in ADMINS:
            await message.answer(f'{message.from_user.first_name} ты не в праве мне указывать!')
        elif not message.reply_to_message:
            await message.answer("отметьте жертву!")
        else:
            await bot.kick_chat_member(message.chat.id,
                                       message.reply_to_message.from_user.id)
            await message.answer(f'Пользователь: @{message.reply_to_message.from_user.username} был изгнан!')
    else:
        await message.answer('это команда работает только в группе!')


# функция закрепа по отметке
async def pin(message: types.Message):
    if message.from_user.id in ADMINS:
        if message.reply_to_message:
            await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
        else:
            await bot.send_message(message.chat.id, 'отметьте для закрепа!')
    else:
        await message.reply('Только для админов!')


# получение всех менторов с возможностью удаления
async def get_all(message: types.Message):
    if message.from_user.id in ADMINS:
        all_mentors = await sql_all()
        await message.answer(f'Все ментора:\n')
        for i in all_mentors:
            await message.answer(f'{i}\n', reply_markup=InlineKeyboardMarkup().add(
                InlineKeyboardButton(f'delete {i[1]}', callback_data=f'delete {i[0]}')))
    else:
        await message.reply('Только для админов!')


# получение случайного ментора
async def get_random_mentor(message: types.Message):
    if message.from_user.id in ADMINS:
        mentors = await sql_all()
        rand_mentor = random.choice(mentors)
        await message.answer(f'{rand_mentor}', reply_markup=InlineKeyboardMarkup().add(
            InlineKeyboardButton(f'delete {rand_mentor[1]}', callback_data=f'delete {rand_mentor[0]}')))
    else:
        await sql_random(message)


# уведомление удаления
async def complete_delete(call: types.CallbackQuery):
    await sql_delete(call.data.replace("delete ", ""))
    await call.answer(text="Удалено", show_alert=True)
    await bot.delete_message(call.from_user.id, call.message.message_id)


# функция регистрации функций
def register_handler_admin(dp: Dispatcher):
    dp.register_message_handler(ban, commands=['ban'], commands_prefix='!/')
    dp.register_message_handler(pin, commands=['pin'], commands_prefix='!')
    dp.register_message_handler(get_all, commands=['get_all'])
    dp.register_message_handler(get_random_mentor, commands=['get'])
    dp.register_callback_query_handler(complete_delete,
                                       lambda call: call.data and call.data.startswith("delete "))
