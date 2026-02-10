import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

# Твой токен
TOKEN = "8502548909:AAFXUrHt7sO2MllBWaq9TTnGugCl4FkEfqM"
# Ссылка на твой сайт (когда опубликуешь на GitHub Pages, замени эту ссылку)
WEBSITE_URL = "https://твой-логин.github.io/название-репозитория/"

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer(
        f"Привет, Жасемочка! ✨\n\nСегодня особенный день, и я подготовил для тебя кое-что интересное. Ты готова?"
    )
    await asyncio.sleep(2)  # Пауза для эффекта ожидания

    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="Да, я готова! ❤️",
        callback_data="step_1")
    )

    await message.answer("Нажми на кнопку ниже, когда будешь готова начать.", reply_markup=builder.as_markup())


@dp.callback_query(lambda c: c.data == "step_1")
async def step_1(callback: types.CallbackQuery):
    await callback.message.edit_text("Сначала я хотел просто написать сообщение... ✍️")
    await asyncio.sleep(2)
    await callback.message.answer("Но потом понял, что этого слишком мало для тебя. 🌹")
    await asyncio.sleep(2)

    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text="Что же дальше? ✨", callback_data="step_2"))
    await callback.message.answer("Хочешь увидеть, что получилось?", reply_markup=builder.as_markup())


@dp.callback_query(lambda c: c.data == "step_2")
async def step_2(callback: types.CallbackQuery):
    await callback.message.answer("Я вложил в это много тепла и воспоминаний... ❤️")
    await asyncio.sleep(3)

    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="ОТКРЫТЬ ПОДАРОК 🎁",
        url=WEBSITE_URL)  # Ссылка на твой сайт
    )

    await callback.message.answer(
        "Нажми на кнопку ниже, чтобы войти в наш маленький мир:",
        reply_markup=builder.as_markup()
    )


async def main():
    print("Бот запущен и ждет Жасемочку...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())