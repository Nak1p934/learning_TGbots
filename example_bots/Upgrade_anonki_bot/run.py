from aiogram import Dispatcher, Bot
import asyncio
from routes import router
from BOT_TOKEN import TOKEN

async def main_less1():
    dp= Dispatcher()
    bot= Bot(token=TOKEN)
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        print("Запуск")
        asyncio.run(main_less1()) 
    except:
        print("Завершение работы")