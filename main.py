import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message()
async def delete_new_system_messages(message: types.Message):
    if message.new_chat_members or message.left_chat_member:
        await message.delete()


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
