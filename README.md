# Репозиторий по изучению aiogram3

Данные репозиторий я делаю для себя что бы повторить материал и для тех кому не понятно обьяснение в интернете

## Базовая конструкция

1. В проекте создаём файл .gitignore 
2. создаём файл BOTTOKEN и там создаём пременную TOKEN названия могут быть любыми
2. В эту переменную вставляем токен бота как строку
3. Создаём папку handlers и в ней файл routes.py в ней будут храниться наши роутеры
4. дальше создаём наш основной файл допустим main.py и пишем туда слудующее -->
from aiogram import Dispatcher, Bot
from BOTTOKEN import TOKEN
import asyncio
from handlers.routes import router


async def main():
    dp = Dispatcher()
    bot = Bot(token=TOKEN)
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main()) 
    except:
        print("Завершение работы")

5. Вот и всё базовая конструкция готова