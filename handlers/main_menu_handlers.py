from config import bot, dp
from tools.check_mac_address_tools import check_availability_mac_address
from tools.check_traffic import get_traffic_info
from aiogram.types import Message
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from keyboards.main_menu_keyboards import generate_main_menu
class FSMDigitnet(StatesGroup):
    check_mac_address = State()
    check_traffic = State()

@dp.message_handler(Text(equals="Проверить мак адрес"))
async def check_mac_address(message: Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id, "Введите ip адрес абонента: \n"
                                    "(формат: X.X.X.X)")
    await FSMDigitnet.check_mac_address.set()



@dp.message_handler(state=FSMDigitnet.check_mac_address)
async def show_mac_address(message: Message, state: FSMContext):
    chat_id = message.chat.id
    ip_address = message.text
    print(ip_address)
    result = check_availability_mac_address(ip_address)
    print(result)
    await bot.send_message(chat_id, result)
    await state.finish()
    await bot.send_message(chat_id, "Выберите, что вас интересует", reply_markup=generate_main_menu())


@dp.message_handler(Text(equals="Проверить трафик абонента"))
async def check_mac_address(message: Message, state: FSMContext):
    await FSMDigitnet.check_traffic.set()
    chat_id = message.chat.id
    await bot.send_message(chat_id, "Введите ip адрес абонента: \n"
                                    "(формат: X.X.X.X)")


@dp.message_handler(state=FSMDigitnet.check_traffic)
async def show_traffic(message: Message, state: FSMContext):
    chat_id = message.chat.id
    result = get_traffic_info(message.text)
    await bot.send_message(chat_id, result)
    await state.finish()
    await bot.send_message(chat_id, "Выберите, что вас интересует", reply_markup=generate_main_menu())





