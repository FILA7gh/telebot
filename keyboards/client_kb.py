from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


# блок кнопок под клавой
start_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
)

# кнопки под клавой
start_button = KeyboardButton('/start')
quiz_button = KeyboardButton('/quiz')
share_location = KeyboardButton('share_locattion', request_location=True)
share_contact = KeyboardButton('share_contact', request_contact=True)
pain_button = KeyboardButton('/pain')
game_button = KeyboardButton('game')

# добавление кнопок в блок
start_markup.add(start_button, quiz_button,
                 share_contact, share_location, pain_button, game_button)
