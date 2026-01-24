from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart
from keyboards import main_keyboard, help_kb, imNotABot_kb, approve_kb
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

router = Router()

class register(StatesGroup):
    nickname = State()
    capcha = State()


@router.message(Command("registration"))
async def registration(message: Message, state: FSMContext):
    await message.answer("Давайте начнём регистрацию на сервер\nДля начал отправте свой nickname в Minecraft")
    await state.set_state(register.nickname)


@router.message(Command("undo"))
async def clear_form(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Заполнение прервано")


@router.message(register.nickname, F.text)
async def poccess_nickname(message: Message, state: FSMContext):
    await state.update_data(nickname=message.text)
    await state.set_state(register.capcha)
    await message.answer("Супер\nТеперь пройдите капчу", reply_markup=imNotABot_kb)


@router.callback_query(register.capcha, F.data == "ready")
async def check_user(callback: CallbackQuery, state: FSMContext, bot: Bot):
    await state.update_data(capcha=True)
    await callback.answer()
    data = await state.get_data()
    await bot.send_message(chat_id="1228798145", text=(
        f"📧 Новая заявка:\n🛐 От @{callback.from_user.username or "Без username"}\n🆔 ID: {callback.from_user.id}\n🦝 Ник в майнкапфе: {data["nickname"]}"), reply_markup=approve_kb(callback.from_user.id))
    await callback.message.answer("Проверка пройденна\nВаша заявка отправленна админу\nОжидайте одобрения")
    await state.clear()


@router.callback_query(F.data.startswith("aplly:"))
async def aplly(callback: CallbackQuery, bot: Bot):
    
    user_id = int(callback.dats.split(":")[1])
    await bot.send_message(chat_id=user_id, text="Ваша заявка одобренна\n IP: ЯНеЕбуКакойТамIP")
    await callback.message.edit_text(callback.message.text + "Заявка одобренна")
    await callback.answer("Заявка одобренна")


@router.callback_query(F.data.startswith("deny:"))
async def aplly(callback: CallbackQuery, bot: Bot):
    user_id = int(callback.dats.split(":")[1])
    await bot.send_message(chat_id=user_id, text="Ваша заявка отклонена")
    await callback.message.edit_text(callback.message.text + "Заявка отклоненна")
    await callback.answer("Заявка Отклонена")


@router.message(CommandStart())
async def start(message: Message):
    await message.answer("Choose your gender", reply_markup=main_keyboard)


@router.message(Command("help"))
async def help(message: Message):
    await message.answer("Start bot - /start \nshow this menu - /help", reply_markup=help_kb)


@router.message()
async def echo(message: Message):
    await message.answer(message.text)