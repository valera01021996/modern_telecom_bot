from config import bot, dp
from aiogram.types import Message
from keyboards.main_menu_keyboards import generate_main_menu


@dp.message_handler(commands=["start"])
async def start(message: Message):
    chat_id = message.chat.id
    full_name = message.chat.full_name
    await bot.send_message(chat_id, "Выберите, что вас интересует", reply_markup=generate_main_menu())


