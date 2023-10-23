from config import bot, dp
from aiogram.types import Message


@dp.message_handler(commands=["start"])
async def start(message: Message):
    chat_id = message.chat.id
    full_name = message.chat.full_name
    await bot.send_message(chat_id, "Введите ip адрес абонента: \n"
                                    "(формат: X.X.X.X)")


