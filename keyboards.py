from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

main_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Men")],
    [KeyboardButton(text="Girl")]
], one_time_keyboard=True)

help_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="google", url="google.com")],
    [InlineKeyboardButton(text="My github", url="https://github.com/Nak1p934/learning_tgbots"), InlineKeyboardButton(text="yandex", url="yandex.ru")]
])

imNotABot_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Я не бот", callback_data="ready")]
])
def approve_kb(user_id: int):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="✅", callback_data=f"aplly:{user_id}"), InlineKeyboardButton(text="❌", callback_data=f"deny:{user_id}")]
    ])