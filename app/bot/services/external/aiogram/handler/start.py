"""
init aiogram
"""
from aiogram import F
from aiogram.types import Message

from app.bot import models
from app.bot.controllers import controller
from app.bot.services.external.aiogram import shortcut
from app.bot.services.external.aiogram.button import markup
from app.bot.services.external.aiogram import dispatcher as dp


@dp.message((F.text == "/start") | (F.text == "🔙 Ortga"))
async def start(message: Message) -> None:
    """
    handler will forward receive a message back to the sender
    """
    chat_id = message.chat.id

    await shortcut.delete_message(message)
    await controller.create_or_update_client(
        await models.build_client(message)
    )

    buttons = markup.genmarkup(["🛍 Maxsulotlar"], [1])

    await message.bot.send_photo(
        chat_id=chat_id,
        photo=models.entrypoint_image,
        caption=models.entrypoint_description,
        reply_markup=buttons,
        parse_mode="html"
    )
