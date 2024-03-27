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
        [InlineKeyboardButton(text="Нет, в следующем", callback_data=f"time.month_1.{city_destination_origin}")],
        [InlineKeyboardButton(text="🏡 Вернуться в меню", callback_data="return_to_menu")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

# Клавиатура для выбора месяца
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
    # Определение количества дней в выбранном месяце
    days_in_month = (datetime.date(year, month + 1, 1) - datetime.date(year, month, 1)).days
    buttons = []
    for day in range(1, days_in_month + 1):
        callback_data = f"time.day_{day}.{month_year_city_destination_origin}"
        buttons.append(InlineKeyboardButton(text=str(day), callback_data=callback_data))
    keyboard_rows = [buttons[i:i+7] for i in range(0, days_in_month, 7)]
    return InlineKeyboardMarkup(inline_keyboard=keyboard_rows)

async def airlines_start():
    buttons = [
        [InlineKeyboardButton(text="Выбрать время", callback_data=f"gdfgdf")],
        [InlineKeyboardButton(text="Спланировать обратный маршрут", callback_data=f"dwertwe")],
        [InlineKeyboardButton(text="🏡 Вернуться в меню", callback_data="return_to_menu")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)