from aiogram import Dispatcher, Bot
import asyncio
from BOTTOKENLESS2 import TOKEN_LESS2


async def main_less2():
    dp_less2 = Dispatcher()
    bot_less2 = Bot()
    dp_less2.include_router(router)
    await dp_less2.start_polling(bot_less2)


if __name__ == "__main__":
    try:
        asyncio.run(main_less2)
    except:
        print("Завершение работы")
