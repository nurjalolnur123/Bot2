from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types.web_app_info import WebAppInfo
from buttons import *
from aiogram.dispatcher.filters import Text



bot = Bot(token="5328846899:AAEhCTY-A3jmeJzbEoSOtP9E4nJjzj6E0Xk")
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    with open('users.txt', 'a') as f:
        f.write('0')
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await message.reply("<b>🔍 Assalomu alaykum men sizga telegramdan chiqmasdan internetdan qidirish imkoniyatini beraman</b>\n<b>👇 Pastdagi tugmalardan o'zingiz xohlagan saytni tanlang</b>", parse_mode='html',reply_markup=keyboard)
    

@dp.message_handler(lambda message: message.text == "Google")
async def google(message: types.Message):
    await message.reply("🔍 Siz Googleni tanladingiz!", parse_mode='html',reply_markup=InlineKeyboardMarkup().add               (InlineKeyboardButton(text="Google",
    web_app=WebAppInfo(url="https://google.com/"))))    

@dp.message_handler(lambda message: message.text == "Yandex")
async def yandex(message: types.Message):
    await message.reply("🔍 Siz Yandexni tanladingiz!", parse_mode='html',reply_markup=InlineKeyboardMarkup().add               (InlineKeyboardButton(text="Yandex",
    web_app=WebAppInfo(url="https://yandex.com/"))))    

@dp.message_handler(lambda message: message.text == "DuckDuckGo")
async def DuckDuckGo(message: types.Message):
    await message.reply("🔍 Siz DuckDuckGoni tanladingiz!", parse_mode='html',reply_markup=InlineKeyboardMarkup().add               (InlineKeyboardButton(text="DuckDuckGo",
    web_app=WebAppInfo(url="https://duckduckgo.com/"))))    

@dp.message_handler(lambda message: message.text == "Bing")
async def Bing(message: types.Message):
    await message.reply("🔍 Siz Bingni tanladingiz!", parse_mode='html',reply_markup=InlineKeyboardMarkup().add               (InlineKeyboardButton(text="Bing",
    web_app=WebAppInfo(url="https://www.bing.com/"))))    

@dp.message_handler(lambda message: message.text == "Brave")
async def Brave(message: types.Message):
    await message.reply("🔍 Siz Braveni tanladingiz!", parse_mode='html',reply_markup=InlineKeyboardMarkup().add               (InlineKeyboardButton(text="Brave",
    web_app=WebAppInfo(url="https://search.brave.com/"))))    

@dp.message_handler(lambda message: message.text == "👨‍💻 Dasturchi")
async def dasturchi(message: types.Message):
    await message.reply("<b>👨‍💻 Dasturchi: @uz_developer_uz @jalol_dev</b>", parse_mode='html')


@dp.message_handler(lambda message: message.text == "📊Foydalanuvchilar")
async def favin(message: types.Message):
    users = 0
    with open('users.txt','r') as r:
        read = r.read()

    for rs in read:
        users+=1
    await message.answer(f"📊Foydalanuvchilar soni: <i>{users}ta</i>", parse_mode='html')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)