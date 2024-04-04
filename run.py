import asyncio

from aiogram.enums import ParseMode
from aiogram.client.bot import DefaultBotProperties
from aiogram import Bot, Dispatcher
from config import TOKEN
from aiogram.fsm.storage.memory import MemoryStorage

import handlers

from db_admin import admin 

from db_admin.models import async_main

async def main():
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(handlers.router_u)
    dp.include_router(admin.router_a)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    
    
if __name__ == '__main__':
    try:
        asyncio.run(async_main())
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Выход')
