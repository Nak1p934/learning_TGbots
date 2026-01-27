from aiogram import Router
from aiogram.types import Message
router_less1 = Router()


@router_less1.message()
async def echo(message: Message):
    await message.answer(f"Ваше сообщение: {message.text}")