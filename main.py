import logging
from config import dp
from aiogram import executor
from handlers import client, extra, callback, admin


# вызов регистров
client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
admin.register_handler_admin(dp)

extra.register_handlers_extra(dp)

# точка входа
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)  # логируем события
    executor.start_polling(dp, skip_updates=True)
