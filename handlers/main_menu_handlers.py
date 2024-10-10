from config import bot, dp
from tools.check_mac_address_tools import check_arp_entry
from tools.check_traffic import get_traffic_info
from tools.check_pppoe import check_pppoe_session
from tools.check_mac_bridge import check_mac_in_bridge_hosts
from aiogram.types import Message
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from keyboards.main_menu_keyboards import generate_main_menu


class FSMDigitnet(StatesGroup):
    check_arp = State()
    check_traffic = State()
    check_pppoe = State()
    check_mac_address = State()


@dp.message_handler(Text(equals="Проверить ARP"))
async def check_arp(message: Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id, "Введите ip адрес абонента: \n"
                                    "(формат: X.X.X.X)")
    await FSMDigitnet.check_arp.set()


@dp.message_handler(state=FSMDigitnet.check_arp)
async def show_arp(message: Message, state: FSMContext):
    chat_id = message.chat.id
    ip_address = message.text
    print(ip_address)
    result = check_arp_entry(ip_address)
    print(result)
    await bot.send_message(chat_id, result)
    await state.finish()
    await bot.send_message(chat_id, "Выберите, что вас интересует", reply_markup=generate_main_menu())


@dp.message_handler(Text(equals="Проверить трафик"))
async def check_traffic(message: Message, state: FSMContext):
    await FSMDigitnet.check_traffic.set()
    chat_id = message.chat.id
    await bot.send_message(chat_id, "Введите ip адрес абонента: \n"
                                    "(формат: X.X.X.X)")


@dp.message_handler(state=FSMDigitnet.check_traffic)
async def show_traffic(message: Message, state: FSMContext):
    chat_id = message.chat.id
    result = get_traffic_info(message.text)
    # await bot.send_message(chat_id, result)
    await bot.send_photo(chat_id, photo=result, caption=f"График текущей скорости по IP адресу: {message.text}")
    await state.finish()
    await bot.send_message(chat_id, "Выберите, что вас интересует", reply_markup=generate_main_menu())


@dp.message_handler(Text(equals="Проверить сессию PPPoE"))
async def check_pppoe(message: Message):
    await FSMDigitnet.check_pppoe.set()
    chat_id = message.chat.id
    await bot.send_message(chat_id, "Введите логин абонента: ")


@dp.message_handler(state=FSMDigitnet.check_pppoe)
async def show_pppoe(message: Message, state: FSMContext):
    chat_id = message.chat.id
    result = check_pppoe_session(message.text.lower())
    await bot.send_message(chat_id, result)
    await state.finish()
    await bot.send_message(chat_id, "Выберите, что вас интересует", reply_markup=generate_main_menu())


@dp.message_handler(Text(equals="Проверить мак адрес на brigde"))
async def check_mac_address(message: Message):
    await FSMDigitnet.check_mac_address.set()
    chat_id = message.chat.id
    await bot.send_message(chat_id, "Введите мак-адрес: \n"
                                    "формат(xx:xx:xx:xx:xx:xx)")


@dp.message_handler(state=FSMDigitnet.check_mac_address)
async def show_mac_address(message: Message, state: FSMContext):
    chat_id = message.chat.id
    result = check_mac_in_bridge_hosts(message.text)
    await bot.send_message(chat_id, result)
    await state.finish()
    await bot.send_message(chat_id, "Выберите, что вас интересует", reply_markup=generate_main_menu())
