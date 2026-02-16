import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart


API_TOKEN = "8083855809:AAEEWBl0R9dIKSDLJxw7GhR0ouLRABkLeB4"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Привіт! Я твій перший бот!")
 ]0

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

#TEST1234