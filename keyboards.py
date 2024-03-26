import datetime
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# Клавиатура - Меню
async def menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="✈️ Построить Маршрут"), KeyboardButton(text="👤 ")],
            [KeyboardButton(text="👥 "), KeyboardButton(text="👥 ")]], 
        resize_keyboard=True, input_field_placeholder="Выберите пункт ниже")

# Клавиатура для возврата в меню
async def return_to_menu():
    return InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="🏡 Вернуться в меню", callback_data="return_to_menu")]])

# Клавиатура со списком городов - вылет
async def city_origin():
    return InlineKeyboardMarkup(inline_keyboard=
        [[
        InlineKeyboardButton(text="Иркутск", callback_data=f"city.origin_IKT"),
        InlineKeyboardButton(text="Москва", callback_data=f"city.origin_MOV"),
        ],[
        InlineKeyboardButton(text="Санкт-Петербург", callback_data=f"city.origin_LED"),
        InlineKeyboardButton(text="Сочи", callback_data=f"city.origin_AER"),
        ],[               
        InlineKeyboardButton(text="Екатеринбург", callback_data=f"city.origin_SVX"),
        InlineKeyboardButton(text="Новосибирск", callback_data=f"city.origin_OVB")
        ],[
        InlineKeyboardButton(text="🏡 Вернуться в меню", callback_data="return_to_menu")]])

# Клавиатура со списком городов - прилет
async def city_destination(city_origin):
    return InlineKeyboardMarkup(inline_keyboard=
        [[
        InlineKeyboardButton(text="Иркутск", callback_data=f"city.destination_IKT.{city_origin}"),
        InlineKeyboardButton(text="Москва", callback_data=f"city.destination_MOV.{city_origin}"),
        ],[
        InlineKeyboardButton(text="Санкт-Петербург", callback_data=f"city.destination_LED.{city_origin}"),
        InlineKeyboardButton(text="Сочи", callback_data=f"city.destination_AER.{city_origin}"),
        ],[               
        InlineKeyboardButton(text="Екатеринбург", callback_data=f"city.destination_SVX.{city_origin}"),
        InlineKeyboardButton(text="Новосибирск", callback_data=f"city.destination_OVB.{city_origin}")
        ],[
        InlineKeyboardButton(text="🏡 Вернуться в меню", callback_data="return_to_menu")]])

# Клавиатура для выбора месяца
async def time_month():
    buttons = [
        [InlineKeyboardButton(text="Январь", callback_data=f"time.month_01"), InlineKeyboardButton(text="Февраль", callback_data=f"time.month_02")],
        [InlineKeyboardButton(text="Март", callback_data=f"time.month_03"), InlineKeyboardButton(text="Апрель", callback_data=f"time.month_04")],
        [InlineKeyboardButton(text="Май", callback_data=f"time.month_05"), InlineKeyboardButton(text="Июнь", callback_data=f"time.month_06")],
        [InlineKeyboardButton(text="Июль", callback_data=f"time.month_07"), InlineKeyboardButton(text="Август", callback_data=f"time.month_08")],
        [InlineKeyboardButton(text="Сентябрь", callback_data=f"time.month_09"), InlineKeyboardButton(text="Октябрь", callback_data=f"time.month_10")],
        [InlineKeyboardButton(text="Ноябрь", callback_data=f"time.month_11"), InlineKeyboardButton(text="Декабрь", callback_data=f"time.month_12")],
        [InlineKeyboardButton(text="🏡 Вернуться в меню", callback_data="return_to_menu")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

# Функция для создания клавиатуры выбора дня месяца
async def create_calendar():
    now = datetime.datetime.now()
    calendar = InlineKeyboardMarkup(row_width=7)
    month = now.month
    year = now.year
    # Определение количества дней в месяце
    days_in_month = (datetime.date(year, month + 1, 1) - datetime.date(year, month, 1)).days
    for day in range(1, days_in_month + 1):
        callback_data = f"time.day_{day}"
        calendar.insert(InlineKeyboardButton(text=str(day), callback_data=callback_data))
    return calendar