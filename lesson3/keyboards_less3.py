from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio

main_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Да"), KeyboardButton(text="Нет")]
], resize_keyboard=True, input_field_placeholder="Ответь на вопрос кнопками", one_time_keyboard=True)

async def coco():
    coco_keyboard = ReplyKeyboardMarkup([
        [KeyboardButton(text="Являюсь")],
        [KeyboardButton(text="Нет😭")]
    ], resize_keyboard=True, input_field_placeholder="Изменил надпись", one_time_keyboard=True)