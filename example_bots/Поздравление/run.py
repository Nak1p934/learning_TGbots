from aiogram import Dispatcher, Bot
import asyncio
from routes import router
from example_bots.Поздравление.BOT_TOKEN import TOKEN
async def main():
    # print("Bot work")
    dp = Dispatcher()
    bot = Bot(token=TOKEN)
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main()) 
    except:
        print("Завершение работы")