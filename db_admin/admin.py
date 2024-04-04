from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup

from aiogram.fsm.context import FSMContext

from config import ADMIN_TELEGRAM_ID

import keyboards as kb

router_a = Router()

class AddAttractionStates(StatesGroup):
    city = State()
    name = State()
    description = State()
    photo = State()

@router_a.message(Command("commands"))
async def start_command(message: Message):
    if message.from_user.id == ADMIN_TELEGRAM_ID:
        await message.answer(f"Список всех доступных команд\n\n"
                             f"/cities - Информация о городах: Добавить/Изменить/Удалить \n\n"
                             f"/ -  \n\n"
                             f"/ -  \n\n"
                             f"/ -  \n\n")                       
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
    city = query.data.split("_")[1]
    await query.message.answer(f"Город - {city}\n\nВыберите действие:", reply_markup=await kb.choose_action(city))
    
@router_a.callback_query(F.data.startswith("choose.attraction.add_"))
async def Choose_city_name(query: CallbackQuery, state: FSMContext):
    city = query.data.split("_")[1]
    await state.update_data(city=city)
    await query.message.answer("Давайте добавим новую достопримечательность. Введите название:")
    await state.set_state(AddAttractionStates.name)
    
@router_a.message(AddAttractionStates.name)
async def Choose_city_description(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Введите описание:")
    await state.set_state(AddAttractionStates.description)

    # data = await state.get_data()
    # await state.clear()
    
@router_a.message(AddAttractionStates.description)
async def Choose_city_description(message: Message, state: FSMContext):
    await state.update_data(description=message.text)
    await message.answer("Отправьте фотографию места")  
    
    # Не реализованный функционал добавления информации по достопримечательностям 
    