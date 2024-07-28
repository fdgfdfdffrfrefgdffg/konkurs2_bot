from aiogram import Bot, Dispatcher
from asyncio import run
from bot_config import BOT_TOKEN
import logging
import message
import callback_data
import data

dp = Dispatcher()

async def main():
    bot = Bot(BOT_TOKEN)
    logging.basicConfig(level=logging.INFO)
    data.default_tasks()
    dp.include_router(message.router)
    dp.include_router(callback_data.router)

    await dp.start_polling(bot, polling_timeout=1)
    data.conn.close()

run(main())