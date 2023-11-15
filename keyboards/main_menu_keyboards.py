from aiogram.types import ReplyKeyboardMarkup, KeyboardButton








def generate_main_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(
        KeyboardButton(text="Проверить мак адрес"),
        KeyboardButton(text="Проверить трафик абонента")
    )
    return markup


