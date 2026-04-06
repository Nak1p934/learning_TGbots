from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from keyboards import example_kb as kb1
from keyboards import reinbow_kb, emoji_kb
import asyncio

router = Router()


@router.callback_query(F.data == "btn1")
async def btn1_handler(callback: CallbackQuery):
    await callback.answer("Уведомление", show_alert=True)

@router.callback_query(F.data == "btn2")
async def btn2_handler(callback: CallbackQuery):
    await callback.answer("Вы нажали кнопку 2")
    await asyncio.sleep(3)
    await callback.message.answer("200")


@router.message(Command("rainbow"))
async def rainbow_handler(message: Message):
    await message.answer(text="Rainbow buttons text text text", reply_markup=reinbow_kb)


@router.message(Command("emoji"))
async def emoji_handler(message: Message):
    await message.answer(text="Emoji buttons text text text", reply_markup=emoji_kb)


@router.message()
async def example_inline_kb(message: Message):
    await message.answer(text="Text text text text", reply_markup=kb1)