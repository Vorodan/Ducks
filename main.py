import asyncio
import os
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, types
from aiogram.types.web_app_info import WebAppInfo
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.fsm.storage.memory import MemoryStorage

load_dotenv()
token_ = os.getenv("bot_token")

dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: types.Message):
    builder = ReplyKeyboardBuilder()
    builder.add(types.KeyboardButton(text='Открыть приложение', web_app=WebAppInfo(url='https://html-preview.github.io/?url=https://github.com/Vorodan/Ducks/blob/main/templates/index.html')))
    await message.answer(text='Привет 😀', reply_markup=builder.as_markup())

async def main() -> None:
    bot = Bot(token_)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())