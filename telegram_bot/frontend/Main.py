from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram import executor

API_TOKEN = '6707293132:AAGMer0gt7hRIwUTSrMxt1NtGCdaeUvEx8w'


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    buttons = [
        types.InlineKeyboardButton(text="Просмотр статистики", callback_data="button1"),
        types.InlineKeyboardButton(text="Напомнить позже", callback_data="button2")
    ]
    keyboard.add(*buttons)
    await message.answer("Выберите кнопку:", reply_markup=keyboard)

@dp.callback_query_handler(lambda c: c.data in ["button2"])
async def process_choice1(callback_query: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    button3 = types.InlineKeyboardButton(text="Получить свою статистику", callback_data="choice1")
    button4 = types.InlineKeyboardButton(text="Получить статистику пользователя", callback_data="choice2")
    keyboard.add(button3, button4)
    await bot.send_message(callback_query.from_user.id, "Выберите одну из", reply_markup=keyboard)

@dp.callback_query_handler(lambda c: c.data in ["choice1", "choice2"])
async def process_choice2(callback_query: types.CallbackQuery):
    if callback_query.data == "choice1":
        await bot.send_message(callback_query.from_user.id, "choice1")     
    elif callback_query.data == "choice2":
        await bot.send_message(callback_query.from_user.id, "choice2")
    


@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    await message.answer("Вам помогут эти команды")

if __name__ == '__main__':
    executor.start_polling(dp)