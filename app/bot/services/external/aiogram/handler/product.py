"""
init aiogram
"""
from aiogram import F
from aiogram.types import Message

from app.bot.services.external.aiogram import shortcut
from app.bot.services.external.aiogram.button import inline
from app.bot.services.external.aiogram import dispatcher as dp


@dp.message(F.text == "🛍 Maxsulotlar")
async def product_handler(message: Message) -> None:
    """
    handler will forward receive a message back to the sender
    """
    await shortcut.delete_message(message)

    await message.bot.send_message(
        chat_id=message.from_user.id,
        text="🛒 Kategoriyalar",
        reply_markup=inline.generate_inline(
            **await shortcut.get_category_actions()
        )
    )
