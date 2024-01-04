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

from config import settings

bot = Bot(token=settings.bot_token.get_secret_value())
dp = Dispatcher()


@dp.message(F.text, Command("start"))
async def send_welcome(message: Message):
    buttons = [
        InlineKeyboardButton(
            text="Просмотр статистики",
            callback_data="button1",
        ),
        InlineKeyboardButton(
            text="Напомнить позже",
            callback_data="button2",
        ),
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=[buttons])
    await message.answer("Выберите кнопку:", reply_markup=keyboard)


@dp.callback_query(lambda c: c.data in ["button2"])
async def process_choice1(callback_query: CallbackQuery):
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


@dp.callback_query(lambda c: c.data in ["choice1", "choice2"])
async def process_choice2(callback_query: CallbackQuery):
    await bot.send_message(
        chat_id=callback_query.from_user.id,
        text=callback_query.data,
    )


@dp.message(Command("help"))
async def send_help(message: Message):
    await message.answer("Вам помогут эти команды")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
