from aiogram import Bot, Dispatcher
import asyncio
from BOT_TOKEN import TOKEN
from routes import router

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(router=router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except:
        print("Завершение работы")