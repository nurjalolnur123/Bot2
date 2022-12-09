from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import WebAppInfo
from aiogram.dispatcher.filters import Text



bot = Bot(token="5809518813:AAHHuCALMR1lrWSzimLEbQUUfYQED7fpQUw")
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    await message.answer("Assalomu alaykum tariflardan birini tanlashingiz mumkin!\n\nDasturchi: @uz_developer_uz @jalol_dev",
reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(text="Tariflarni ochish",
web_app=WebAppInfo(url="https://nurjalolnur123.github.io/"))))




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)