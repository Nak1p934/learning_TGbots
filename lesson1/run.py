from aiogram import Dispatcher, Bot # Импортируем нашего бота и диспетчер
import asyncio # Импортируем asyncio
from routes_for_lesson1 import router_less1 # Имортируем переменну нашего роутера из routes.py
from BOTTOKEN_LESS1 import TOKEN1 # Токен нашего бота


async def main_less1(): # Наша основная функция
    dp_less1 = Dispatcher() # Переменная с диспетчером
    bot_less1 = Bot(token=TOKEN1) # Переменная с ботом
    dp_less1.include_router(router_less1)
    await dp_less1.start_polling(bot_less1) # Начало работы


if __name__ == "__main__": # Проверка на то не импортируется файл 
    try:
        asyncio.run(main_less1()) 
    except:
        print("Завершение работы") # Сообзение о том что бот завершил работу 
# Завершить работу можно с помощью Ctrl + C
# У меня файлы называются по другому что бы отличать уроки