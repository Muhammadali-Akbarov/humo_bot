"""
category handler
"""
from aiogram.types import CallbackQuery

from app.bot.controllers import controller
from app.bot.services.external.aiogram import dispatcher as dp


@dp.callback_query()
async def category(cb: CallbackQuery) -> None:
    """
    handler will forward receive a message back to the sender
    """
    chat_id = cb.message.chat.id

    category_id = cb.data

    results = await controller.get_products(
        category_id=category_id
    )

    if not results:
        await cb.message.bot.send_message(
            chat_id=chat_id,
            text="Bu kategoriyada maxsulot topilmadi"
        )
        return

    for result in results:
        name = result.name
        photo = result.file_id
        description = result.description

        await cb.message.bot.send_photo(
            chat_id=chat_id,
            photo=photo,
            caption=f"{name}\n\n{description}\n\nMurojat uchun:  ☎️ 97 985 38 00" # noqa
        )
