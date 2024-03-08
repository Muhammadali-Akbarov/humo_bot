"""
init aiogram
"""
from aiogram import F
from aiogram.types import Message

from app.bot.controllers import controller
from app.bot.services.external.aiogram.button import inline
from app.bot.services.external.aiogram import dispatcher as dp
from app.bot.services.external.aiogram.shortcut import get_schema


@dp.message(F.text == "🛍 Maxsulotlar")
async def product_handler(message: Message) -> None:
    """
    Handler will forward receive a message back to the sender
    """
    actions = []

    categories = await controller.get_categories()

    for category in categories:
        actions.append({
            "text": category.name,
            "callback_data": str(category.id)
        })

    schema = get_schema(len(categories))

    inline_button = inline.generate_inline(
        actions=actions,
        schema=schema
    )

    await message.bot.send_message(
        chat_id=message.from_user.id,
        text="🛒 Kategoriyalar",
        reply_markup=inline_button
    )
