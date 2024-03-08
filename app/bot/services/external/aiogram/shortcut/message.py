"""
init message shortcuts
"""
from aiogram.types import Message


async def delete_message(message: Message):
    """
    delete message shortcut
    """
    await message.bot.delete_message(
        chat_id=message.chat.id,
        message_id=message.message_id,
        request_timeout=1
    )
