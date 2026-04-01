from aiogram.types import ReplyKeyboardMarkup, KeyboardButton # Импортируем класс кнопок
import asyncio

main_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Да"), KeyboardButton(text="Нет")]
], resize_keyboard=True, input_field_placeholder="Ответь на вопрос кнопками", one_time_keyboard=True)
# Структура кнопок


async def coco():
    coco_keyboard = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="Являюсь")],
        [KeyboardButton(text="Нет")]
], resize_keyboard=True, input_field_placeholder="Изменил надпись", one_time_keyboard=True)
    return coco_keyboard