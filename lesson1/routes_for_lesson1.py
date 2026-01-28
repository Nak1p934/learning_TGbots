from aiogram import Router # Импортируем роутер
from aiogram.types import Message # Импортируем тим данных Message
router_less1 = Router() # Создаём переменную с роутером


# Если бы роутер что то обрабатывал то в скобках что то было, например CommandStart()
@router_less1.message() # Наш первый роутер который обрабатывает всё
async def echo(message: Message): # Ассинхронная функция которая принимает сообщение
    await message.answer(f"Ваше сообщение: {message.text}") # Ответ от Бота пользователю через message.answer туда мы передаём строку
# Через f строку мы подставляем сообщение пользователя ^ с помощью message.text
# Happy pythoning!