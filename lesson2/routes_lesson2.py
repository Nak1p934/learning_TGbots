from aiogram.filters import Command, CommandStart
from aiogram import Router
from aiogram.types import Message
router_less2 = Router()


@router_less2.message(CommandStart())
async def start(message: Message):
    await message.answer("Добро пожаловать в нашего бота!")


@router_less2.message(Command("send_hi"))
async def send_hi(message: Message):
    await message.answer("Hi!")


@router_less2.message(Command("help"))
async def help(message: Message):
    await message.answer("Вот список команд:")
    await message.answer("/start\n/help\n/send_hi")


@router_less2.message()
async def nothing(message: Message):
    await message.reply("Такой команды нет😓")