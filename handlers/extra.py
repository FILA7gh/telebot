from random import choice
from aiogram import types, Dispatcher
from config import bot, ADMINS


# проверка цензурных слов для участников
async def censorship_check(message: types.Message):

    bad_words = ['java', 'fuck', 'лох', 'даун',
                 'ебать', 'сука', 'бл', 'епта']

    username = f"@{message.from_user.username}" \
               if message.from_user.username is not None else message.from_user.first_name

    for word in bad_words:
        if word in message.text.lower().replace(' ', ''):
            if message.from_user.id not in ADMINS:
                await bot.send_message(message.chat.id, f'"{username}" это слово зaпрещено админом!')
                await bot.delete_message(message.chat.id, message.message_id)
            # для админов
            else:
                await message.reply(f'Вам можно)')

    # рандомная игра для админа
    if message.text.lower().startswith('game'):
        if message.from_user.id in ADMINS:
            games = ['⚽', '🏀', '🎰', '🎯', '🎳', '🎲']
            rand_game = choice(games)
            await bot.send_dice(message.chat.id, emoji=rand_game)
        else:
            await message.answer('команда только для админов!')


# регистрация функций
def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(censorship_check)
