from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

example_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Кнопка 1", callback_data="btn1"), #callback_data - обязательный параметр для inline клавиатур или подставьте url
     InlineKeyboardButton(text="Кнопка 2", callback_data="btn2")],
])

reinbow_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="PRIMARY", style="primary", callback_data="primary", )],
    [InlineKeyboardButton(text="SUCCESS", style="success", callback_data="success")],
    [InlineKeyboardButton(text="DANGER", style="danger", callback_data="danger")]
])

emoji_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="YouTube", url="https://www.youtube.com", icon_custom_emoji_id="5334681713316479679", style="danger"), InlineKeyboardButton(text="GitHub", url="https://github.com/Nak1p934/learning_TGbots", style="success", icon_custom_emoji_id="5346181118884331907")]
])