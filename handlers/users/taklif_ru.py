from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from keyboards.default.menu import only_menu_ru, bosh_menu_ru, firmalar
from loader import bot, dp


class ShikoyatState_ru(StatesGroup):
    firma = State()
    taklif = State()


class TaklifState_ru(StatesGroup):
    firma = State()
    taklif = State()


@dp.message_handler(text="🏠Главное меню", state=[ShikoyatState_ru.taklif, TaklifState_ru.taklif])
async def ta234232k(message: types.Message, state:FSMContext):
    await message.answer(f"Выберите нужный раздел.\n"
                         f"Ваша личная информация будет храниться конфиденциально.", reply_markup=bosh_menu_ru)
    await state.finish()


@dp.message_handler(text="🏠Главное меню")
async def ta234232k(message: types.Message):
    await message.answer(f"Выберите нужный раздел.\n"
                         f"Ваша личная информация будет храниться конфиденциально.", reply_markup=bosh_menu_ru)


@dp.message_handler(text="✅Предложение")
async def taklik(message: types.Message):
    await message.answer(f"Выбор фирмы", reply_markup=firmalar)
    await TaklifState_ru.firma.set()


@dp.message_handler(state=TaklifState_ru.firma)
async def ta234242(message: types.Message, state: FSMContext):
    await state.update_data(
        {"firma": message.text}
    )
    await message.answer(f"напишите свое предложение.", reply_markup=only_menu_ru)
    await TaklifState_ru.taklif.set()


@dp.message_handler(state=TaklifState_ru.taklif)
async def takl43332h2(message: types.Message, state: FSMContext):
    data = await state.get_data()
    firma = str(data.get("firma"))
    text = f"<b>✅TAKLIF</b>\n\n" + firma + f"\n" + message.text
    try:
        await bot.send_message(chat_id="7010118152", text=text)
        await bot.send_message(chat_id="6921491661", text=text)
    except:
        pas=1
    await message.answer(f"Информация отправлена", reply_markup=bosh_menu_ru)
    await state.finish()


@dp.message_handler(text="❗Жалоба")
async def ta12ik(message: types.Message):
    await message.answer(f"Выбор фирмы.", reply_markup=firmalar)
    await ShikoyatState_ru.firma.set()


@dp.message_handler(state=ShikoyatState_ru.firma)
async def t343242(message: types.Message, state: FSMContext):
    await state.update_data(
        {"firma": message.text}
    )
    await message.answer(f"напишите вашу жалобу.", reply_markup=only_menu_ru)
    await ShikoyatState_ru.taklif.set()


@dp.message_handler(state=ShikoyatState_ru.taklif)
async def ta21ish2(message: types.Message, state: FSMContext):
    data = await state.get_data()
    firma = str(data.get("firma"))
    text = f"<b>❗SHIKOYAT</b>\n\n" + firma + f"\n" + message.text
    try:
        await bot.send_message(chat_id="7010118152", text=text)
        await bot.send_message(chat_id="6921491661", text=text)
    except:
        pas=1
    await message.answer(f"Информация отправлена", reply_markup=bosh_menu_ru)
    await state.finish()
