"""
init aiogram
"""
from aiogram.types import Message
from aiogram.filters import CommandStart

from app.bot.services.external.aiogram import dispatcher as dp


@dp.message(CommandStart())
async def echo_handler(message: Message) -> None:
    """
    Handler will forward receive a message back to the sender
    """
    await message.answer("Humo savdo markazi botiga xush kelibsiz!")
