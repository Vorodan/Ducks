from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть приложение', web_app=WebAppInfo(url='https://html-preview.github.io/?url=https://github.com/Vorodan/Ducks/blob/main/index.html')))
    await message.answer('Привет 😀', reply_markup=markup)

executor.start_polling(dp)