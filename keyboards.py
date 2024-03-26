from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


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

async def city_destination(city_origin):
    return InlineKeyboardMarkup(inline_keyboard=
        [[
        InlineKeyboardButton(text="Иркутск", callback_data=f"city.destination_IKT_{city_origin}"),
        InlineKeyboardButton(text="Москва", callback_data=f"city.destination_MOV_{city_origin}"),
        ],[
        InlineKeyboardButton(text="Санкт-Петербург", callback_data=f"city.destination_LED_{city_origin}"),
        InlineKeyboardButton(text="Сочи", callback_data=f"city.destination_AER_{city_origin}"),
        ],[               
        InlineKeyboardButton(text="Екатеринбург", callback_data=f"city.destination_SVX_{city_origin}"),
        InlineKeyboardButton(text="Новосибирск", callback_data=f"city.destination_OVB_{city_origin}")
        ],[
        InlineKeyboardButton(text="🏡 Вернуться в меню", callback_data="return_to_menu")]])

async def return_to_menu():
    return InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="🏡 Вернуться в меню", callback_data="return_to_menu")]])