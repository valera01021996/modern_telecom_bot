from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
import os

load_dotenv()
bot = Bot(os.getenv("BOT_TOKEN"))
dp = Dispatcher(bot)

