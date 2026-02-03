from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Да"), KeyboardButton(text="Нет")]
], resize_keyboard=True, input_field_placeholder="Ответь на вопрос кнопками", one_time_keyboard=True)