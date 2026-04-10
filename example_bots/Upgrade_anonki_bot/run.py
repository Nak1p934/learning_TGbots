from aiogram import Dispatcher, Bot
import asyncio
from routes import router
from BOT_TOKEN import TOKEN
from middleware import AntiSpamMiddleware

async def main_less1():
    dp= Dispatcher()
    bot= Bot(token=TOKEN)
    dp.include_router(router)
    dp.message.middleware(AntiSpamMiddleware())
    dp.callback_query.middleware(AntiSpamMiddleware())
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        print("Запуск")
        asyncio.run(main_less1()) 
    except:
        print("Завершение работы")