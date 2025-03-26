import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command('rm_old_msgs'))
async def rm_old_sys_msg(message: types.Message):
    for message_id in range(9, 135):
        await bot.delete_message(chat_id='2589587595', message_id=message_id)


@dp.message()
async def delete_new_system_messages(message: types.Message):
    if message.new_chat_members or message.left_chat_member or message.pinned_message:
        await message.delete()


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
