from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
# from aiogram import types
from aiogram.filters import CommandStart


import keyboards as kb

router_u = Router()


@router_u.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f'Привет 👋🏼,\nЯ - чат-бот Travel Tracker\n\n'
                             f'Что умеет этот бот?: \n\n'
                             f'• Мы можем построить дальний маршрут из точки А в точку Б\n'  
                             f'• Вы сможете увидеть актуальную информацию об автобусных, железнодорожных и аэро-маршрутах в России\n'

                             f'А также предостовить информацию по авиакомпниям')
    await message.answer(f'🔮 Главное меню', reply_markup=await kb.menu())

        
@router_u.message(F.text == 'Построить маршрут')
async def Kassa(message: Message):
    await message.answer(f'Выберите кассу, чтобы узнать подробную информацию:', reply_markup=await kb.kassa())

@router_u.callback_query(F.data.startswith("city.origin_"))
async def Kassa_inf(query: CallbackQuery):
    city_origin = int(query.data.split("_")[1])
    await query.message.answer("Касса не найдена.", reply_markup=await kb.return_to_menu())