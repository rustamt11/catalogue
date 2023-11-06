import sys
import asyncio
import logging

from app.database.models import async_main
from aiogram import Bot, Dispatcher
from config import TOKEN
from app.handlers import router

async def main():
    await async_main()

    bot = Bot(token=TOKEN, parse_mode="HTML")
    dp = Dispatcher()
    dp.include_router(router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
