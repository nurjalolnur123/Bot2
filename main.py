from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types.web_app_info import WebAppInfo
from buttons import *
from aiogram.dispatcher.filters import Text



bot = Bot(token="5814538074:AAHq3nsKZQgeJMNPInPrBvvGr1Oo0XdtuBk")
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    with open('users.txt', 'a') as f:
        f.write('0')
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите способ подачи"
    )
    await message.reply("<b>🍏 Assalomu alaykum men sizga telegramdan chiqmasdan apple.com saytidagi mahsulotlarni topib beraman!</b>\n<b>👇 Pastdagi tugmalardan o'zingiz xohlagan mahsulotni tanlang</b>\n\n<i>🍏 Olmani tishlab qo'yish esdan chiqibdi*</i>", parse_mode='html',reply_markup=keyboard)
    

@dp.message_handler(lambda message: message.text == "💻 Mac")
async def macbook(message: types.Message):
    await message.reply("💻 Barcha Maclarni ko'rish uchun <i>💻 Mac</i> ni ustiga bosing!", parse_mode='html',reply_markup=InlineKeyboardMarkup().add               (InlineKeyboardButton(text="💻 Mac",
    web_app=WebAppInfo(url="https://www.apple.com/mac/"))))    

@dp.message_handler(lambda message: message.text == "📱 Iphone")
async def iphone(message: types.Message):
    await message.reply("📱 Barcha Iphonelarni ko'rish uchun <i>🎧 AirPods</i> ni ustiga bosing!", parse_mode='html',reply_markup=InlineKeyboardMarkup().add               (InlineKeyboardButton(text="📱 Iphone",
    web_app=WebAppInfo(url="https://www.apple.com/iphone/"))))

@dp.message_handler(lambda message: message.text == "🎧 AirPods")
async def airpod(message: types.Message):
    await message.reply("🎧 Barcha AirPodlarni ko'rish uchun <i>🎧 AirPods</i> ni ustiga bosing!", parse_mode='html',reply_markup=InlineKeyboardMarkup().add               (InlineKeyboardButton(text="🎧 AirPods",
    web_app=WebAppInfo(url="https://www.apple.com/airpods/"))))

@dp.message_handler(lambda message: message.text == "📱 Ipad")
async def ipad(message: types.Message):
    await message.reply("📱 Barcha AirPodlarni ko'rish uchun <i>📱 Ipad</i> ni ustiga bosing!", parse_mode='html',reply_markup=InlineKeyboardMarkup().add               (InlineKeyboardButton(text="📱 Ipad",
    web_app=WebAppInfo(url="https://www.apple.com/ipad/"))))

@dp.message_handler(lambda message: message.text == "⌚️ Watch")
async def watch(message: types.Message):
    await message.reply("⌚️ Barcha Watchlarni ko'rish uchun <i>⌚️ Watch</i> ni ustiga bosing!", parse_mode='html',reply_markup=InlineKeyboardMarkup().add               (InlineKeyboardButton(text="⌚️ Watch",
    web_app=WebAppInfo(url="https://www.apple.com/watch/"))))

@dp.message_handler(lambda message: message.text == "📺 Apple TV & Home")
async def tv(message: types.Message):
    await message.reply("📺 Barcha Watchlarni ko'rish uchun <i>📺 Apple TV & Home</i> ni ustiga bosing!", parse_mode='html',reply_markup=InlineKeyboardMarkup().add               (InlineKeyboardButton(text="📺 Apple TV & Home",
    web_app=WebAppInfo(url="https://www.apple.com/tv-home/"))))

@dp.message_handler(lambda message: message.text == "🍏 Apple veb-sayti")
async def appleweb(message: types.Message):
    await message.reply("🍏 Apple veb-saytini ko'rish uchun <i>🍏 Apple veb-sayti</i> ni ustiga bosing!", parse_mode='html',reply_markup=InlineKeyboardMarkup().add               (InlineKeyboardButton(text="🍏 Apple veb-sayti",
    web_app=WebAppInfo(url="https://www.apple.com"))))

@dp.message_handler(lambda message: message.text == "✅ Aksessuarlar")
async def aksessuarlar(message: types.Message):
    await message.reply("✅ Barcha aksessuarlarni ko'rish uchun <i>✅ Aksessuarlar</i> ni ustiga bosing!", parse_mode='html',reply_markup=InlineKeyboardMarkup().add               (InlineKeyboardButton(text="✅ Aksessuarlar",
    web_app=WebAppInfo(url="https://www.apple.com/shop/accessories/all"))))

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