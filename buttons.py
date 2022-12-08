from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup,KeyboardButton

kb = [
        [
            types.KeyboardButton(text="💻 Mac"),
            types.KeyboardButton(text="📱 Iphone"),
            types.KeyboardButton(text="🎧 AirPods"),
        ],
        [
            types.KeyboardButton(text="📱 Ipad"),
            types.KeyboardButton(text="⌚️ Watch"),
            types.KeyboardButton(text="📺 Apple TV & Home"),
        ],
        [
            types.KeyboardButton(text="🍏 Apple veb-sayti"),
            types.KeyboardButton(text="✅ Aksessuarlar"),
            types.KeyboardButton(text="📊Foydalanuvchilar")
        ],
        [
            types.KeyboardButton(text="🧑‍💻 Dasturchi")
        ],
    ]
