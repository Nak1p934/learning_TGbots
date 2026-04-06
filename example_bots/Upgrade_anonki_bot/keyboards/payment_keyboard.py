from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

payment_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Подарить за 15 XTR", pay=True)]
])