import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

API_TOKEN = "8782231469:AAHVZBLyDzHWdJYO5q9jCz25DjCIlB55IP0"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

async def wait_and_remind(chat_id, text, minutes):  
    await asyncio.sleep(minutes * 60)
    await bot.send_message(chat_id, f"час вийшов!\nЗавдання: {text}")

@dp.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer(
        "привіт, я бот нагадувач!\n"
        "пиши так: `'Назва справи' через '1' (кількість хвилин)`",
        reply_markup=types.ReplyKeyboardRemove()
    )

@dp.message()
async def handle_message(message: types.Message):
    
    if " через " in message.text.lower():
        try:
            parts = message.text.lower().split(" через ")
            task_text = parts[0].strip()
            time_minutes = int(parts[1].strip())

            await message.answer(f"нагадаю про '{task_text}' через {time_minutes} хв.")
            asyncio.create_task(wait_and_remind(message.chat.id, task_text, time_minutes))
            
        except ValueError:
            await message.answer(" помилка: після слова 'через' має бути число (хвилини).")
    else:
        await message.answer("я тебе не зрозумів. Напиши наприклад: `Сходити в магазин через 5`")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
#bot reminder