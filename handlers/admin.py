from config import ADMINS, bot
from aiogram import types, Dispatcher


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
            await message.answer(f'Пользователь: {message.reply_to_message.from_user.username} был изгнан!')
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


# регистрация функций
def register_handler_admin(dp: Dispatcher):
    dp.register_message_handler(ban, commands=['ban'], commands_prefix='!/')
    dp.register_message_handler(pin, commands=['pin'], commands_prefix='!')
