from aiogram import Bot, Dispatcher
import asyncio
from BOTTOKEN_LESS3 import TOKEN_LESS3
from routes_less3 import router

async def main():
    bot = Bot(token=TOKEN_LESS3)
    dp = Dispatcher()
    dp.include_router(router=router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except:
        print("Завершение работы")