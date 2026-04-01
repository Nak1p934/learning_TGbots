from aiogram.types import Message
from aiogram import Router, F # Не обращайте внимание на это разберём потом
from aiogram.filters import Command
from keyboards_less3 import main_kb, coco # Импорт клавиатур

router = Router()

@router.message(Command("test"))
async def test_reply(message: Message): 
    await message.answer(text="Вы старше 18 лет?", reply_markup=main_kb) # Выбераем нашу клавиатуру


@router.message(F.text == "Да") # Не обращайте внимание, забегая вперёд скажу что это фильтр
async def new_kb(message: Message):
    await message.reply(f"Вы гражданин Японии?", reply_markup=await coco()) # клавиатура результат выполнения функции

@router.message(Command("info"))
async def info(message: Message):
    await message.answer(f'''
Id: {message.from_user.id}
Username: {message.from_user.username}
Firstname: {message.from_user.first_name}
Lastname: {message.from_user.last_name}
Language: {message.from_user.language_code}
Is prem: {message.from_user.is_premium}
Is bot: {message.from_user.is_bot}
added_to_attachment_menu(Хз че это, перевод: Добавленно в меню вложений): {message.from_user.added_to_attachment_menu}
can_connect_to_business: {message.from_user.can_connect_to_business}
can_join_groups: {message.from_user.can_join_groups}
can_read_all_group_messages: {message.from_user.can_read_all_group_messages}
has_main_web_app: {message.from_user.has_main_web_app}
model_config: {message.from_user.model_config} 
supports_inline_queries: {message.from_user.supports_inline_queries}
Всё...
''')
# Кто нибудь разберитесь что делает model_config
# Happy pythoning <3