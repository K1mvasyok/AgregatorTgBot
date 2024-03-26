from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
# from aiogram import types
from aiogram.filters import CommandStart


import keyboards as kb
from config import ADMIN_TELEGRAM_ID

router_u = Router()


@router_u.message(CommandStart())
async def cmd_start(message: Message):
    if message.from_user.id == ADMIN_TELEGRAM_ID:
        await message.answer(f'Привет 👋🏼,\nЯ - чат-бот АВИАКОМПАНИИ\n\n'
                             f'Я могу показать и взаимодействовать: \n\n'
                             f'• Кассами\n'  
                             f'• Кассирами\n'
                             f'• Клиентами\n'
                             f'• Купонами\n'
                             f'• Билетами\n\n'
                             f'А также предостовить информацию по авиакомпниям')
        await message.answer(f'🔮 Главное меню', reply_markup=await kb.menu())
    else:
        await message.answer(f'Меню администратора\n\n'
                             f'Я могу показать и взаимодействовать\n'
                             f'• Кассами\n'
                             f'• Кассиры\n'
                             f'• Клиентами\n'
                             f'• Купонами\n'
                             f'• Билетами\n'
                             f'Отчёты и взаимойдествия с авиакомпаниями по команде /commands')
        await message.answer(f'🔮 Главное меню', reply_markup=await kb.menu())
        
        
@router_u.message(F.text == '💳 Касса')
async def Kassa(message: Message):
    await message.answer(f'Выберите кассу, чтобы узнать подробную информацию:', reply_markup=await kb.kassa())

@router_u.callback_query(F.data.startswith("kassa_number:"))
async def Kassa_inf(query: CallbackQuery):
    kassa_id = int(query.data.split(":")[1])
    await query.message.answer("Касса не найдена.", reply_markup=await kb.return_to_menu())