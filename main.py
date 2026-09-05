import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from config import BOT_TOKEN

bot = Bot(token = BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Hello! I am your bot.")

@dp.message(Command("help"))
async def help_command(message: Message):
    await message.answer("This is the help command. How can I assist you?")

@dp.message(Command("about"))
async def about_command(message: Message):
    await message.answer("This bot is created to demonstrate basic command handling using")

@dp.message(F.text.lower() == 'пока') 
async def cmd_buy(message: Message):
    await message.answer("Пока! Буду рад видеть тебя снова!")

async def main():
    # logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    # logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

        