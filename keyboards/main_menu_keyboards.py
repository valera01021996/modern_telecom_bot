from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def generate_main_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.row(
        KeyboardButton(text="Проверить ARP"),
        KeyboardButton(text="Проверить трафик")
    )
    markup.row(KeyboardButton(text="Проверить сессию PPPoE"))
    markup.row(KeyboardButton(text="Проверить мак адрес на brigde"))
    return markup
