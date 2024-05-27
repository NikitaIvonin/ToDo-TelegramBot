import asyncio
from aiogram import Bot, Dispatcher

from handlers import router
from database import create_database, connect_database, create_table


async def main():
    create_database()
    connect_database()
    create_table()
    bot = Bot(token='6451589117:AAFrcNyNafKCbKSJhdGZ-k9XAzmj4EWna1A')
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен")