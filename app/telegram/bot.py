import asyncio
import logging
from aiogram import Bot, Dispatcher
from app.telegram.handlers import router


logging.basicConfig(level=logging.INFO)

bot = Bot(token="7217637541:AAFmcDDbJiNDXYieR9jyV1OYVvaYBCWyXFM")

dp = Dispatcher()

dp.include_routers(router)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())