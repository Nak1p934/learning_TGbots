from aiogram import Router, F
from aiogram.filters import Command, CommandStart, CommandObject
from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import asyncio

router = Router()

class Form(StatesGroup):
    send_message_id = State()

users = []
admins = []


@router.message(CommandStart(deep_link=True))
async def start(message: Message, command: CommandObject, state: FSMContext):
    # if str(message.from_user.id) != command.args:
        #print(command.args, message.from_user.id, message.from_user.id != command.args, type(command.args), type(message.from_user.id))
    await message.answer("Готов отправить сообщение")
    await state.set_state(Form.send_message_id)
    await state.update_data(send_message_id=command.args)
    if message.from_user.id not in users:
            users.append(message.from_user.id)
            #print(users)
    # else:
    #     await message.answer("Вы перешли по своей же ссылке")


@router.message(CommandStart(deep_link=False))
async def start(message: Message, command: CommandObject, state: FSMContext):
    await message.answer("Приветствую, я бот для анонимных сообщений.\nОтправь мне сообщение и я передам его!")
    await message.answer("Отправь мне /get что бы я дал тебе ссылку для отправки сообщения тебе")
    if message.from_user.id not in users:
        users.append(message.from_user.id)
        #print(users)


@router.message(Command("clear"))
async def clear(message: Message, state: FSMContext):
    await state.clear()


@router.message(Command("Send_message_all"))
async def spam(message: Message):
    for i in users:
        try:
            await message.bot.send_message(chat_id=i, text=message.text[18:])
        except:
            pass


@router.message(Command("get"))
async def get_link(message: Message):
    await message.answer(f"Вот твоя ссылка для отправки сообщения тебе: t.me/pizdASK_bot?start={message.from_user.id}")


@router.message(Command("Send_ls"))
async def send_message_direct(message: Message):
    await message.bot.send_message(chat_id=message.text.split()[1], text=message.text[(10 + len(message.text.split()[1])):])


@router.message(F.reply_to_message)
async def handle_reply(message: Message):
    if message.reply_to_message.from_user.id == message.bot.id and message.reply_to_message.text.rfind("https://web.telegram.org/a/#") != -1:
        #print(message.reply_to_message.text.rfind("t.me/"))
        #print(message.reply_to_message.text[(message.reply_to_message.text.rfind("t.me/") + 5):])
        await message.bot.send_message(chat_id= message.reply_to_message.text[(message.reply_to_message.text.rfind("https://web.telegram.org/a/#") + 28):], text=message.text)
    else:
        pass


@router.message(F.text)
async def send_message(message: Message, state: FSMContext):
    try:
        data =await state.get_data()
        await message.bot.send_message(chat_id= data.get("send_message_id"), text=f"У вас новое сообщение!<blockquote>{message.text}</blockquote>", parse_mode="HTML")
        await message.bot.send_message(chat_id= data.get("send_message_id"), text=f"Сообщение от {message.from_user.first_name}:\n{message.text}\nВНИМАНИЕ, если вы хотите ответить на сообщение то отвечайти именно на ЭТО сообщение, а не на то, что выше\nЕсли имени нет вот ссылка: https://web.telegram.org/a/#{message.from_user.id}")
        await message.answer("Сообщение успешно отправлено!")
    except Exception as e:
        await message.answer("Произошла ошибка при отправке сообщения.")
        #print(f"Ошибка при отправке сообщения: {e}")
