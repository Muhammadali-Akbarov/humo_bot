"""
entrypoints
"""
import asyncio

from app.bot.services.external.aiogram import bot
from app.bot.services.external.aiogram import handler
from app.bot.settings.internal.conf.bot import IS_WEBHOOK_ENABLED


async def main() -> None:
    """
    entrypoint of running bot operations
    """
    if IS_WEBHOOK_ENABLED is False:
        await bot.delete_webhook(drop_pending_updates=True)
        await handler.dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
