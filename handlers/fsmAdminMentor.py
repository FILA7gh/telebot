from random import randint
from config import ADMINS
from keyboards.client_kb import submit_markup, cancel_markup, directory_markup
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


#  Создание состояний ФСМ
class FSMAdmin(StatesGroup):
    name = State()
    direction = State()
    age = State()
    group = State()
    submit = State()


#  приватная функция старта ФСМ
async def fsm_start(message: types.Message):
    if message.from_user.id in ADMINS:
        if message.chat.type == 'private':
            await FSMAdmin.name.set()
            await message.answer('Введите имя ментора:', reply_markup=cancel_markup)
        else:
            await message.reply('Команда работает только в личке!')
    else:
        await message.answer('Команда только для админов!')


# функция записи имени
async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['id'] = id_gen()
        if message.text.isalpha():
            data['name'] = message.text
            await FSMAdmin.next()
            await message.answer('Введите направление ментора:', reply_markup=directory_markup)
        else:
            await message.answer('Введите корректное имя!')


# функция записи направления
async def load_direction(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['direction'] = message.text
        await FSMAdmin.next()
        await message.answer('Введите возраст ментора:', reply_markup=cancel_markup)


# функция записи возраста
async def load_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text.isdigit() and 0 < int(message.text) < 100:
            data['age'] = message.text
            await FSMAdmin.next()
            await message.answer('Введите название группы:', reply_markup=cancel_markup)
        else:
            await message.answer('Введите коректный возраст!')


# функция записи группы
async def load_group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:

        data['group'] = message.text
        # данные
        mentor_data = message.answer(
                                 f"ID: {data['id']}\n"
                                 f"Имя: {data['name']}\n"
                                 f"Направление: {data['direction']}\n"
                                 f"Возраст: {data['age']}\n"
                                 f"Группа: {data['group']}\n\n"
                                )
        await mentor_data  # вывод данных
    await FSMAdmin.next()
    await message.answer('Все верно?', reply_markup=submit_markup)


# функция для подтверждения
async def submit(message: types.Message, state: FSMContext):

    if message.text.lower() == "да":
        # DB
        await state.finish()
        await message.answer('Загружено в базу данных')

    elif message.text.lower() == 'нет':
        await state.finish()
        await message.answer('Ну если не нравится перерегистрируйся')

    else:
        await message.answer('Введите "ДА" или "НЕТ"')


# функция отмены ФСМ
async def cancel_reg(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer("отменено")


# генератор айди
def id_gen():
    new_id = ''
    for i in range(10):
        new_id += str(randint(0, 9))
    return new_id


# функция регистрации функций
def register_handler_fsm(dp: Dispatcher):
    dp.register_message_handler(cancel_reg, state='*', commands='CANCEL')
    dp.register_message_handler(fsm_start, commands=['req'])
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_direction, state=FSMAdmin.direction)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_group, state=FSMAdmin.group)
    dp.register_message_handler(submit, state=FSMAdmin.submit)
