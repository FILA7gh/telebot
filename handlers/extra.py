from aiogram import types, Dispatcher
from decouple import config
import openai
from weather import weather


openai.api_key = config("OPENAI_API_KEY")


# chat GPT
def get_message(message):
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=message.text,
      temperature=0.5,
      max_tokens=1000,
      top_p=1.0,
      frequency_penalty=0.5,
      presence_penalty=0.0,
    )

    return response['choices'][0]['text']


async def openai_(message: types.Message):

    if message.text.startswith('weather'):
        await message.answer(weather(message.text.replace('weather', '')))

    else:
        await message.answer(get_message(message))


# функция регистрации функций
def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(openai_)
