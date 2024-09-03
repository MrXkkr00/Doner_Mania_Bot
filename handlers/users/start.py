from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.menu import bosh_menu, bosh_menu_ru
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    f = open("./data/reklama.txt", "r")
    text = f.read()
    if not str(user_id) in text:
        f = open("./data/reklama.txt", "a")
        f.write(f"{user_id}\n")
        f.close()

    await message.answer(f"Kerakli bo'limni tanlang.\n"
                         f"Sizning Shaxsiy ma'lumotlaringiz sir tutiladi", reply_markup=bosh_menu)


@dp.message_handler(text="🇷🇺 Русский")
async def bot_s1t(message: types.Message):
    await message.answer(f"Выберите нужный раздел.\n"
                         f"Ваша личная информация будет храниться в тайне", reply_markup=bosh_menu_ru)


@dp.message_handler(text="🇺🇿 O'zbek")
async def bot_s112t(message: types.Message):
    await message.answer(f"Kerakli bo'limni tanlang.\n"
                         f"Sizning Shaxsiy ma'lumotlaringiz sir tutiladi", reply_markup=bosh_menu)



