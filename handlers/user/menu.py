from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from loaders import dp
from keyboards.default import menu


@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await message.answer("Assalaumagaleikum", reply_markup=menu)
    await message.answer("Bireuin tanda", reply_markup=menu)


@dp.message_handler(Text(equals=["2E", "4E", "3I"]))
async def get_food(message: Message):
    await  message.answer(f"Tandaldy {message.text}. Rahmet", reply_markup=ReplyKeyboardRemove())