import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart

API_TOKEN = "8388385129:AAEjfKcq4bP09lO-YvVWYNfiq6KQK07R9n0"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Привіт. Я твій перший бот")

var = 0

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())