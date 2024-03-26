from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

import keyboards as kb

router_u = Router()

# Команда старт
@router_u.message(CommandStart())
async def Cmd_start(message: Message):
    await message.answer(f'Привет 👋🏼,\nЯ - чат-бот Travel Tracker\n\n'
                             f'Что умеет этот бот?: \n\n'
                             f'• Мы можем построить дальний маршрут из точки А в точку Б\n\n'  
                             f'• Вы сможете увидеть актуальную информацию об автобусных, железнодорожных и аэро-маршрутах в России')
    await message.answer(f'🔮 Главное меню', reply_markup=await kb.menu())

# Возврат в меню
@router_u.callback_query(F.data.startswith("return_to_menu"))
async def Return_to_menu(query: CallbackQuery):
    await query.message.answer('🔮 Главное меню', reply_markup=await kb.menu())

# Реакция на кнопку построить маршрут
@router_u.message(F.text == '✈️ Построить Маршрут')
async def Сity_origin_botton(message: Message):
    await message.answer(f'Выберите город отправления:', reply_markup=await kb.city_origin())

@router_u.callback_query(F.data.startswith("city.origin_"))
async def City_destination_botton(query: CallbackQuery):
    city_origin = query.data.split("_")[1]
    await query.message.answer(f'Выберите город ?прилета?:', reply_markup=await kb.city_destination(city_origin))