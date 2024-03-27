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

# Клавиаутра для выбора год
async def time_year(city_destination_origin):
    buttons = [
        [InlineKeyboardButton(text="Да, в этом году", callback_data=f"time.year_0.{city_destination_origin}")],
        [InlineKeyboardButton(text="Нет, в следующем", callback_data=f"time.year_1.{city_destination_origin}")],
        [InlineKeyboardButton(text="🏡 Вернуться в меню", callback_data="return_to_menu")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

# Клавиатура для выбора месяца вылета
async def time_month(city_destination_origin):
    buttons = [
        [InlineKeyboardButton(text="Январь", callback_data=f"time.month_01.{city_destination_origin}"), InlineKeyboardButton(text="Февраль", callback_data=f"time.month_02.{city_destination_origin}")],
        [InlineKeyboardButton(text="Март", callback_data=f"time.month_03.{city_destination_origin}"), InlineKeyboardButton(text="Апрель", callback_data=f"time.month_04.{city_destination_origin}")],
        [InlineKeyboardButton(text="Май", callback_data=f"time.month_05.{city_destination_origin}"), InlineKeyboardButton(text="Июнь", callback_data=f"time.month_06.{city_destination_origin}")],
        [InlineKeyboardButton(text="Июль", callback_data=f"time.month_07.{city_destination_origin}"), InlineKeyboardButton(text="Август", callback_data=f"time.month_08.{city_destination_origin}")],
        [InlineKeyboardButton(text="Сентябрь", callback_data=f"time.month_09.{city_destination_origin}"), InlineKeyboardButton(text="Октябрь", callback_data=f"time.month_10.{city_destination_origin}")],
        [InlineKeyboardButton(text="Ноябрь", callback_data=f"time.month_11.{city_destination_origin}"), InlineKeyboardButton(text="Декабрь", callback_data=f"time.month_12.{city_destination_origin}")],
        [InlineKeyboardButton(text="🏡 Вернуться в меню", callback_data="return_to_menu")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

# Функция для создания клавиатуры выбора дня месяца
async def time_day(month_year_city_destination_origin, month, year_offset=0):
    now = datetime.datetime.now()
    year = now.year + year_offset  # Вычисляем год с учетом смещения
    next_month = month + 1 if month < 12 else 1  # Учитываем переход на следующий год
    next_year = year + 1 if month == 12 else year 
    days_in_month = (datetime.date(next_year, next_month, 1) - datetime.date(year, month, 1)).days # Определение количества дней в выбранном месяце
    buttons = []
    for day in range(1, days_in_month + 1):
        callback_data = f"time.day_{day}.{month_year_city_destination_origin}"
        buttons.append(InlineKeyboardButton(text=str(day), callback_data=callback_data))
    keyboard_rows = [buttons[i:i+7] for i in range(0, days_in_month, 7)]
    keyboard_rows.append([InlineKeyboardButton(text="🏡 Вернуться в меню", callback_data="return_to_menu")])
    return InlineKeyboardMarkup(inline_keyboard=keyboard_rows)

async def airlines_start(day_month_year_city_destination_origin):
    buttons = [
        [InlineKeyboardButton(text="🕒 Выбрать время", callback_data=f"sdgdf")],
        [InlineKeyboardButton(text="🔁 Спланировать обратный маршрут", callback_data=f"airlines.back_{day_month_year_city_destination_origin}")],
        [InlineKeyboardButton(text="🏡 Вернуться в меню", callback_data="return_to_menu")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

# Клавиатура для выбора месяца прилета
async def back_month(day_month_year_city_destination_origin):
    buttons = [
        [InlineKeyboardButton(text="Январь", callback_data=f"back.month_01.{day_month_year_city_destination_origin}"), InlineKeyboardButton(text="Февраль", callback_data=f"back.month_02.{day_month_year_city_destination_origin}")],
        [InlineKeyboardButton(text="Март", callback_data=f"back.month_03.{day_month_year_city_destination_origin}"), InlineKeyboardButton(text="Апрель", callback_data=f"back.month_04.{day_month_year_city_destination_origin}")],
        [InlineKeyboardButton(text="Май", callback_data=f"back.month_05.{day_month_year_city_destination_origin}"), InlineKeyboardButton(text="Июнь", callback_data=f"back.month_06.{day_month_year_city_destination_origin}")],
        [InlineKeyboardButton(text="Июль", callback_data=f"back.month_07.{day_month_year_city_destination_origin}"), InlineKeyboardButton(text="Август", callback_data=f"back.month_08.{day_month_year_city_destination_origin}")],
        [InlineKeyboardButton(text="Сентябрь", callback_data=f"back.month_09.{day_month_year_city_destination_origin}"), InlineKeyboardButton(text="Октябрь", callback_data=f"back.month_10.{day_month_year_city_destination_origin}")],
        [InlineKeyboardButton(text="Ноябрь", callback_data=f"back.month_11.{day_month_year_city_destination_origin}"), InlineKeyboardButton(text="Декабрь", callback_data=f"back.month_12.{day_month_year_city_destination_origin}")],
        [InlineKeyboardButton(text="🏡 Вернуться в меню", callback_data="return_to_menu")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

# Функция для создания клавиатуры выбора дня месяца
async def back_day(backmonth_day_month_year_city_destination_origin, month, year_offset=0):
    now = datetime.datetime.now()
    year = now.year + year_offset  # Вычисляем год с учетом смещения
    next_month = month + 1 if month < 12 else 1  # Учитываем переход на следующий год
    next_year = year + 1 if month == 12 else year 
    days_in_month = (datetime.date(next_year, next_month, 1) - datetime.date(year, month, 1)).days # Определение количества дней в выбранном месяце
    buttons = []
    for day in range(1, days_in_month + 1):
        callback_data = f"back.day_{day}.{backmonth_day_month_year_city_destination_origin}"
        buttons.append(InlineKeyboardButton(text=str(day), callback_data=callback_data))
    keyboard_rows = [buttons[i:i+7] for i in range(0, days_in_month, 7)]
    keyboard_rows.append([InlineKeyboardButton(text="🏡 Вернуться в меню", callback_data="return_to_menu")])
    return InlineKeyboardMarkup(inline_keyboard=keyboard_rows)