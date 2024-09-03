from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from keyboards.default.menu import only_menu, bosh_menu, firmalar
from loader import dp, bot


class ShikoyatState(StatesGroup):
    firma = State()
    taklif = State()


class TaklifState(StatesGroup):
    firma = State()
    taklif = State()


@dp.message_handler(text="🏠Bosh menu", state=[ShikoyatState.taklif, TaklifState.taklif])
async def ta234232k(message: types.Message, state: FSMContext):
    await message.answer(f"Kerakli bo'limni tanlang.\n"
                         f"Sizning Shaxsiy ma'lumotlaringiz sir tutiladi", reply_markup=bosh_menu)
    await state.finish()


@dp.message_handler(text="🏠Bosh menu")
async def ta234232k(message: types.Message, state: FSMContext):
    await message.answer(f"Kerakli bo'limni tanlang.\n"
                         f"Sizning Shaxsiy ma'lumotlaringiz sir tutiladi", reply_markup=bosh_menu)
    await state.finish()


@dp.message_handler(text="✅Taklif")
async def taklik(message: types.Message):
    await message.answer(f"Firmani tanlang.", reply_markup=firmalar)
    await TaklifState.firma.set()


@dp.message_handler(state=TaklifState.firma)
async def ta234242(message: types.Message, state: FSMContext):
    await state.update_data(
        {"firma": message.text}
    )
    await message.answer(f"Taklifingizni yuboring", reply_markup=only_menu)
    await TaklifState.taklif.set()


@dp.message_handler(state=TaklifState.taklif)
async def takli32h2(message: types.Message, state: FSMContext):
    data = await state.get_data()
    firma = str(data.get("firma"))
    text = f"<b>✅TAKLIF</b>\n\n" + firma + f"\n" + message.text
    try:
        await bot.send_message(chat_id="7010118152", text=text)
        await bot.send_message(chat_id="6921491661", text=text)
    except:
        pas = 1
    await message.answer(f"Ma'lumot yuborildi", reply_markup=bosh_menu)
    await state.finish()


@dp.message_handler(text="❗Shikoyat")
async def ta12ik(message: types.Message):
    await message.answer(f"Firmani tanlang", reply_markup=firmalar)
    await ShikoyatState.firma.set()


@dp.message_handler(state=ShikoyatState.firma)
async def ta234242(message: types.Message, state: FSMContext):
    await state.update_data(
        {"firma": message.text}
    )
    await message.answer(f"Shikoyatingizni yuboring.", reply_markup=only_menu)
    await ShikoyatState.taklif.set()


@dp.message_handler(state=ShikoyatState.taklif)
async def ta21ish2(message: types.Message, state: FSMContext):
    data = await state.get_data()
    firma = str(data.get("firma"))
    text = f"<b>❗SHIKOYAT</b>\n\n" + firma + f"\n" + message.text
    try:
        await bot.send_message(chat_id="7010118152", text=text)
        await bot.send_message(chat_id="6921491661", text=text)
    except:
        pas = 1
    await message.answer(f"Ma'lumot yuborildi", reply_markup=bosh_menu)
    await state.finish()


@dp.message_handler(text_contains="ishtimoiy tarmoqlar")
@dp.message_handler(text_contains="и деловые сети")
async def tawrwrre(message: types.Message):
    await message.answer(f"<b>Instagram - Doner Mania</b>\n"
                         f"<b>Instagram - Panasia</b>\n"
                         f"https://www.instagram.com/donermania.uz?igsh=MW5uMnZqbzE3d3llZA%3D%3D&utm_source=qr\n\n")
    await message.answer(f"https://www.instagram.com/panasia.uz?igsh=emo1ZWY2eXA3Y2xn\n")
    await message.answer(f"<b>You tube</b>\n"
                         f"https://youtube.com/@donermania?feature=shared\n")
    await message.answer(f"<b>Tik Tok</b>\n"
                         f"https://www.tiktok.com/@donermania_uz?_t=8mVQqq6om88&_r=1\n")
