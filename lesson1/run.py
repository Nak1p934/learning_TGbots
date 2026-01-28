from aiogram import Dispatcher, Bot
import asyncio
from routes_for_lesson1 import router_less1
from BOTTOKEN_LESS1 import TOKEN1


async def main_less1():
    dp_less1 = Dispatcher()
    bot_less1 = Bot(token=TOKEN1)
    dp_less1.include_router(router_less1)
    await dp_less1.start_polling(bot_less1)


if __name__ == "__main__":
    try:
        asyncio.run(main_less1()) 
    except:
        print("Завершение работы")