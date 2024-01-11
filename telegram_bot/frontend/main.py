import asyncio

from aiogram import (
    Bot,
    Dispatcher,
    F,
)
from aiogram.filters import Command
from aiogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
)

from bot_answers import (
    welcome_text,
    registration_text,
)
from config import settings

bot = Bot(token=settings.bot_token.get_secret_value())
dp = Dispatcher()


@dp.message(F.text, Command("start"))
async def send_welcome(message: Message):
    buttons = [
        InlineKeyboardButton(
            text="Зарегистрировать никнейм",
            callback_data="button1",
        ),
        InlineKeyboardButton(
            text="Напомнить позже",
            callback_data="button2",
        ),
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=[buttons])
    await message.answer(welcome_text)
    await message.answer("Выберите кнопку:", reply_markup=keyboard)


@dp.callback_query(F.data == "button1")
async def process_registration(callback_query: CallbackQuery):
    await bot.send_message(
        text=registration_text,
        chat_id=callback_query.from_user.id,
    )


@dp.callback_query(F.data == "button2")
async def process_button2(callback_query: CallbackQuery):
    buttons = [
        InlineKeyboardButton(
            text="Получить свою статистику",
            callback_data="choice1",
        ),
        InlineKeyboardButton(
            text="Получить статистику пользователя",
            callback_data="choice2",
        ),
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=[buttons])
    await bot.send_message(
        callback_query.from_user.id,
        "Выберите одну из",
        reply_markup=keyboard,
    )


# @dp.callback_query(F.data in ["choice1", "choice2"])
# async def process_choices(callback_query: CallbackQuery):
#     await callback_query.message.answer(text=registration_text)


@dp.message(F.text, Command("help"))
async def send_help(message: Message):
    await message.answer("Вам помогут эти команды")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
