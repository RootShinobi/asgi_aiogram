from aiogram import Dispatcher, Bot
from aiogram.types import Message
from aiogram.filters.command import Command

dp = Dispatcher()
bot = Bot(token="1:A")

@dp.message(Command("ping"))
async def ping(message: Message):
    pass
