import asyncio

from aiogram import Bot, Dispatcher
from config import TOKEN
import handlers


async def main():
    bot = Bot(token=TOKEN, parse_mode='HTML')
    dp = Dispatcher()
    dp.include_router(handlers.router_u)
    await dp.start_polling(bot)
    
    
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Выход')
