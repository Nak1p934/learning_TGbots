from aiogram import Router, F
from aiogram.filters import Command, CommandStart, CommandObject
from aiogram.types import Message, LabeledPrice, PreCheckoutQuery, ContentType, FSInputFile
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import asyncio
from db.session import SessionLocal
from db.crud import add_sms, get_json
import time
from keyboards.payment_keyboard import payment_kb as pay_kb

router = Router()

class Form(StatesGroup):
    send_message_id = State()

users = []


@router.message(CommandStart(deep_link=True))
async def start(message: Message, command: CommandObject, state: FSMContext):
    if str(message.from_user.id) != command.args:
        print(command.args, message.from_user.id, message.from_user.id != command.args, type(command.args), type(message.from_user.id))
        await message.answer("Готов отправить сообщение")
        await state.set_state(Form.send_message_id)
        await state.update_data(send_message_id=command.args)
        if message.from_user.id not in users:
            users.append(message.from_user.id)
            #print(users)
    else:
        await message.answer("Вы перешли по своей же ссылке")


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


@router.message(Command("buy"))
async def send_invoice_hr(message: Message):
    prices = [LabeledPrice(label="XTR", amount=15)]
    await message.answer_invoice(
        title="Подарить мишку",
        description="Сделать подарок анонимно",
        prices=prices,
        provider_token="",
        payload="bear",
        currency="XTR",
        reply_markup=pay_kb
    )


@router.pre_checkout_query()
async def pre_checkout(q: PreCheckoutQuery):
    await q.answer(ok=True)


@router.message(F.content_type == ContentType.SUCCESSFUL_PAYMENT)
async def successful_payment(message: Message, state: FSMContext):
    data =await state.get_data()
    photo = FSInputFile("5372819198003844740.jpg")
    await message.bot.send_photo(chat_id=data.get("send_message_id"), photo=photo)
    await message.bot.send_message(chat_id=data.get("send_message_id"), text="Вам отправили подарок!")


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
        try:
            async with SessionLocal() as session:
                await add_sms(message.from_user.id, int(message.reply_to_message.text[(message.reply_to_message.text.rfind("https://web.telegram.org/a/#") + 28):]), "operator", message.text, time.strftime("%H:%M"))
        except Exception as e:
            print(e)
    else:
        pass


@router.message(F.text)
async def send_message(message: Message, state: FSMContext):
    try:
        data =await state.get_data()
        await message.bot.send_message(chat_id= data.get("send_message_id"), text=f"У вас новое сообщение!<blockquote>{message.text}</blockquote>", parse_mode="HTML")
        await message.bot.send_message(chat_id= data.get("send_message_id"), text=f"Сообщение от {message.from_user.first_name}:\n{message.text}\nВНИМАНИЕ, если вы хотите ответить на сообщение то отвечайти именно на ЭТО сообщение, а не на то, что выше\nЕсли имени нет вот ссылка: https://web.telegram.org/a/#{message.from_user.id}")
        await message.answer("Сообщение успешно отправлено!")
        # print(message.)
        async with SessionLocal() as session:
            await add_sms(int(data.get("send_message_id")), message.from_user.id, "user", message.text, time.strftime("%H:%M"))
    except Exception as e:
        await message.answer("Произошла ошибка при отправке сообщения.")
        print(f"Ошибка при отправке сообщения: {e}")
