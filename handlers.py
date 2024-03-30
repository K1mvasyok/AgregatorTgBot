from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

import datetime

import keyboards as kb
from aviasales import tickets_for_day

router_u = Router()

# Команда старт
@router_u.message(CommandStart())
async def Cmd_start(message: Message):
    await message.answer(f'Привет 👋🏼,\nЯ - чат-бот TravelB\n\n'
                             f'Что умеет этот бот?: \n\n'
                             f'• Мы можем построить дальний маршрут из точки А в точку Б\n\n'  
                             f'• Вы сможете увидеть актуальную информацию аэро-маршрутах в России')
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
    city_origin, city_destination = city_destination_origin.rsplit('.', 1)
    if city_origin == city_destination:
        await query.message.answer("Город отправления и город прибытия не могут совпадать.", reply_markup= await kb.return_to_menu())
        return
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
    month = int(month_year_city_destination_origin.split(".")[0])
    year = int(query.data.split(".")[2])
    await query.message.answer(f'День вылета:', reply_markup=await kb.time_day(month_year_city_destination_origin, month, year))
    
# Продолжение работы с построением маршрутов - вывод информации
@router_u.callback_query(F.data.startswith("time.day_"))
async def Airlines_info(query: CallbackQuery):
    day_month_year_city_destination_origin = query.data.split("_")[1]
    day = int(day_month_year_city_destination_origin.split(".")[0])
    month = int(day_month_year_city_destination_origin.split(".")[1])
    
    now = datetime.datetime.now()
    year_offset = int(day_month_year_city_destination_origin.split(".")[2])
    year = now.year + year_offset
    
    city_origin = day_month_year_city_destination_origin.split(".")[-1]
    city_destination= day_month_year_city_destination_origin.split(".")[3]
    
    tickets, links = await tickets_for_day(day, month, year, city_origin, city_destination)
    
    await query.message.answer(f'{tickets}', reply_markup=await kb.airlines_start(day_month_year_city_destination_origin, links))
    
# Продолжение работы с построением маршрутов - месяц прилёта 
@router_u.callback_query(F.data.startswith("airlines.back_"))
async def Airlines_back_month(query: CallbackQuery):
    day_month_year_city_destination_origin = query.data.split("_")[1]
    await query.message.answer(f'Месяц прилёта:', reply_markup=await kb.back_month(day_month_year_city_destination_origin))
    
# Продолжение работы с построением маршрутов - день прилёта 
@router_u.callback_query(F.data.startswith("back.month_"))
async def Airlines_back_month(query: CallbackQuery):
    backmonth_day_month_year_city_destination_origin = query.data.split("_")[1]
    backmonth = int(backmonth_day_month_year_city_destination_origin.split(".")[0])
    backyear = int(backmonth_day_month_year_city_destination_origin.split(".")[2])
    await query.message.answer(f'День прилёта:', reply_markup=await kb.back_day(backmonth_day_month_year_city_destination_origin, backmonth, backyear)) 
    
@router_u.callback_query(F.data.startswith("back.day_"))
async def Airlines_back_month(query: CallbackQuery):
    day_backmonth_day_month_year_city_destination_origin = query.data.split("_")[1]
    
    city_origin = day_backmonth_day_month_year_city_destination_origin.split(".")[-1]
    city_destination = day_backmonth_day_month_year_city_destination_origin.split(".")[-2]
     
    now = datetime.datetime.now()
    year_offset = int(day_backmonth_day_month_year_city_destination_origin.split(".")[4])
    year = now.year + year_offset
    
    day_start = int(day_backmonth_day_month_year_city_destination_origin.split(".")[2])
    month_start = int(day_backmonth_day_month_year_city_destination_origin.split(".")[3])
    
    day_end = int(day_backmonth_day_month_year_city_destination_origin.split(".")[0])   
    month_end = int(day_backmonth_day_month_year_city_destination_origin.split(".")[1])
    
    tickets = await tickets_for_day(day_start, month_start, year, city_origin, city_destination)
    
    if datetime.datetime(year, month_start, day_start) >= datetime.datetime(year, month_end, day_end):
        await query.message.answer("Дата отправления должна быть раньше даты прибытия.", reply_markup= await kb.return_to_menu())
        return
    
    await query.message.answer(f'Ваши данные:\n\n'
                               f'Дата вылета: {day_start}.{month_start}.{year}\n'
                               f'Дата прилёта: {day_end}.{month_end}.{year}\n'
                               f'Код города вылета: {city_origin}\n'
                               f'Код город прилёта: {city_destination}\n\n'
                               f'{tickets}') 
                            #    reply_markup=await kb.airlines_start())