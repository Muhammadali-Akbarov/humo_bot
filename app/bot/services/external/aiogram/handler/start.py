"""
init aiogram
"""
from aiogram import F
from aiogram.types import Message

from app.bot import models
from app.bot.controllers import controller

from app.bot.services.external.aiogram.button import markup
from app.bot.services.external.aiogram import dispatcher as dp


@dp.message((F.text == "/start") | (F.text == "🔙 Ortga"))
async def start(message: Message) -> None:
    """
    Handler will forward receive a message back to the sender
    """
    client = models.Client(
        chat_id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name
    )
    await controller.create_or_update_client(
        client=client
    )

    btns = ["🛍 Maxsulotlar"]
    schema = [1]

    buttons = markup.genmarkup(btns, schema)

    await message.bot.send_photo(
        chat_id=client.chat_id,
        photo=models.entrypoint_image,
        caption=models.entrypoint_description,
        reply_markup=buttons,
        parse_mode="html"
    )
