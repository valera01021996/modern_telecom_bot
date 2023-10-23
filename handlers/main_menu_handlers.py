from config import bot, dp
from tools.check_mac_address_tools import check_availability_mac_address
from aiogram.types import Message

@dp.message_handler()
async def show_availability_mac_adresss(message: Message):
    chat_id = message.chat.id
    result = check_availability_mac_address(message.text)
    await bot.send_message(chat_id, result)
    await bot.send_message(chat_id, "Введите ip адрес абонента: \n"
                                    "(формат: X.X.X.X)")


