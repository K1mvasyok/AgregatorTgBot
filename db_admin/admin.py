from aiogram import F, Router
from aiogram.types import Message, CallbackQuery, Command

from aiogram.fsm.context import FSMContext

from config import ADMIN_TELEGRAM_ID

import keyboards as kb

router_a = Router()

@router_a.message(Command("commands"))
async def start_command(message: Message):
    if message.from_user.id == ADMIN_TELEGRAM_ID:
        await message.answer(f"Список всех доступных команд\n\n"
                             f"/cities - Информация о городах: Добавить/Изменить/Удалить \n\n"
                             f"/ -  \n\n"
                             f"/ -  \n\n"
                             f"/-  \n\n")                       
    else:
        await message.answer("У вас нет прав на выполнение этой команды.")
        
@router_a.message(Command("cities"))
async def Сities(message: Message):
    if message.from_user.id == ADMIN_TELEGRAM_ID:
        await message.answer(f'Выберите город:', reply_markup=await kb.choose_city())  
    else:
        await message.answer("У вас нет прав на выполнение этой команды.")
        
@router_a.callback_query(F.data.startswith("choose.city_"))
async def Choose_city(query: CallbackQuery):
    city = int(query.data.split("_")[1])
    