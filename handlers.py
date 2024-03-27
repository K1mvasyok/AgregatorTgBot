from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

import datetime

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

# Реакция на кнопку построить маршрут - города вылета 
@router_u.message(F.text == '✈️ Построить Маршрут')
async def Сity_origin_botton(message: Message):
    await message.answer(f'Выберите город отправления:', reply_markup=await kb.city_origin())

# Продолжение работы с построением маршрутов - города прилёта  
@router_u.callback_query(F.data.startswith("city.origin_"))
async def City_destination_botton(query: CallbackQuery):
    city_origin = query.data.split("_")[1]
    await query.message.answer(f'Выберите город ?прилета?:', reply_markup=await kb.city_destination(city_origin))

# Продолжение работы с построением маршрутов - год вылета 
@router_u.callback_query(F.data.startswith("city.destination_"))
async def Time_year_botton(query: CallbackQuery):
    city_destination_origin = query.data.split("_")[1]
    await query.message.answer(f'Планируете полететь в этом году?', reply_markup=await kb.time_year(city_destination_origin))
    
# Продолжение работы с построением маршрутов - месяц вылета   
@router_u.callback_query(F.data.startswith("time.year_"))
async def Time_month_botton(query: CallbackQuery):
    year_city_destination_origin = query.data.split("_")[1]
    await query.message.answer(f'Месяц вылета:', reply_markup=await kb.time_month(year_city_destination_origin))
    
# Продолжение работы с построением маршрутов - день 
@router_u.callback_query(F.data.startswith("time.month_"))
async def Time_day_botton(query: CallbackQuery):
    month_year_city_destination_origin = query.data.split("_")[1]
    month = int(query.data.split("_")[1].split(".")[0])
    year = int(query.data.split(".")[2])
    await query.message.answer(f'День вылета:', reply_markup=await kb.time_day(month_year_city_destination_origin, month, year))
    
@router_u.callback_query(F.data.startswith("time.day_"))
async def Time_month_destination(query: CallbackQuery):
    day_month_year_city_destination_origin = query.data.split("_")[1]
    print(day_month_year_city_destination_origin)
    day = int(day_month_year_city_destination_origin.split(".")[0])
    month = int(day_month_year_city_destination_origin.split(".")[1])
    
    now = datetime.datetime.now()
    year_offset = int(day_month_year_city_destination_origin.split(".")[2])
    year = now.year + year_offset
    
    city_origin = day_month_year_city_destination_origin.split(".")[-1]
    city_destination= day_month_year_city_destination_origin.split(".")[3]
    
    await query.message.answer(f'Ваши данные:\n\n'
                               f'Дата вылета: {day}.{month}.{year}\n'
                               f'Город вылета: {city_origin}\n'
                               f'Город прилёта: {city_destination}', 
                               reply_markup=await kb.airlines_start())