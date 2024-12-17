from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo
from dotenv import load_dotenv
import logging
import os

load_dotenv()
bot = Bot(token=os.getenv('token'))
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("Открыть веб приложение",web_app=WebAppInfo(url='https://startapp.pythonanywhere.com/')))
    await message.answer('Привет', reply_markup=markup)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


@dp.message_handler(commands="help")
async def help_user(message: types.Message):
    await message.reply('Это бот предназначен для веб приложения нажмите кнопку которая привязанная к вашей клавиатуре')

if __name__ == '__main__':
    logging.info('Бот запущен!')
    executor.start_polling(dp)
