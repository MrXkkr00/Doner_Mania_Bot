from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

bosh_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="✅Taklif"),
            KeyboardButton(text="❗Shikoyat"),
        ],
        [
            KeyboardButton(text="🌐Bizning ishtimoiy tarmoqlar"),
        ],
        [
            KeyboardButton(text="🇷🇺 Русский"),
        ]
    ], resize_keyboard=True
)

bosh_menu_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="✅Предложение"),
            KeyboardButton(text="❗Жалоба"),
        ],
        [
            KeyboardButton(text="🌐Наши деловые сети"),
        ],
        [
            KeyboardButton(text="🇺🇿 O'zbek"),
        ]
    ], resize_keyboard=True
)


only_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🏠Bosh menu')
        ]
    ], resize_keyboard=True
)


only_menu_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🏠Главное меню')
        ]
    ], resize_keyboard=True
)

firmalar = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Panasia"),
            KeyboardButton(text="Doner mania"),
        ]
    ], resize_keyboard=True
)