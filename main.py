import asyncio
import logging
from config import dp, bot, ADMINS
from aiogram import executor
from handlers import client, extra, callback, admin, fsmAdminMentor, notification
from database.painbot_db import create_db


async def on_startup(_):
    asyncio.create_task(notification.scheduler())
    await bot.send_message(chat_id=ADMINS[0],
                           text="Bot started!")
    create_db()


# вызов регистров
client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
admin.register_handler_admin(dp)
fsmAdminMentor.register_handler_fsm(dp)
notification.register_handler_notification(dp)

extra.register_handlers_extra(dp)

# точка входа
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)  # логируем события
    executor.start_polling(dp, skip_updates=True,
                           on_startup=on_startup)
