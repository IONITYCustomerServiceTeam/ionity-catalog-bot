
from aiogram import Bot, Dispatcher, types
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
import logging
import os

API_TOKEN = os.getenv('API_TOKEN')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

web_app_url = "https://ionity.ua/shop"

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    keyboard = InlineKeyboardMarkup().add(
        InlineKeyboardButton("КАТАЛОГ", web_app=WebAppInfo(url=web_app_url))
    )
    await message.answer(
        "Дякуємо, що завітали до IONITY!\nНатисніть кнопку нижче, щоб перейти до каталогу:",
        reply_markup=keyboard
    )

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
