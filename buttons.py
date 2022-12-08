from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup,KeyboardButton

kb = [
        [
            types.KeyboardButton(text="Google"),
            types.KeyboardButton(text="Yandex"),
            types.KeyboardButton(text="DuckDuckGo"),
        ],
        [
            types.KeyboardButton(text="Bing"),
            types.KeyboardButton(text="Brave"),
            types.KeyboardButton(text="📊Foydalanuvchilar")
        ]
    ]
