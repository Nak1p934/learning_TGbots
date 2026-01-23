from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart
from keyboards import main_keyboard, help_kb, imNotABot_kb
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
    await message.answer("Супер\nТеперь пройдите капчу", reply_markup=imNotABot_kb)


@router.callback_query(register.capcha, F.data == "ready")
async def check_user(callback: CallbackQuery, state: FSMContext):
        await state.update_data(capha=True)
        await callback.message.answer("Проверка пройденна")
        await state.clear()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer("Choose your gender", reply_markup=main_keyboard)


@router.message(Command("help"))
async def help(message: Message):
    await message.answer("Start bot - /start \nshow this menu - /help", reply_markup=help_kb)


@router.message()
async def echo(message: Message):
    await message.answer(message.text)