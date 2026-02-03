from aiogram.types import ReplyKeyboardMarkup, keyboard_button, Message
from aiogram import Router
from aiogram.filters import Command
from keyboards_less3 import main_kb

router = Router()

@router.message(Command("test"))
async def test_reply(message: Message):
    await message.answer(text="Вы старше 18 лет?", reply_markup=main_kb)