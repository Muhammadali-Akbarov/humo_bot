"""
entry point of the application where
FastAPI app is created and routes are defined.
"""
import fastapi

from app.bot.presentation import router
from app.bot.services.external.aiogram import bot
from app.bot.settings.internal.conf import port

app = fastapi.FastAPI()


@app.on_event("startup")
async def startup_event():
    """
    startup events.
    """
    await bot.send_message(
        chat_id=2105729169,
        text="✅ Humo bot has been started"
    )
    await bot.set_webhook(
        url=f"{port.SERVICE_ADDRESS}/v1/humo/bot/webhook/",
        drop_pending_updates=True
    )


@app.on_event("shutdown")
async def on_shutdown():
    """
    shutdown events.
    """
    await bot.send_message(
        chat_id=2105729169,
        text="🔥️️️️️️ Humo bot's shutting down"
    )
    await bot.session.close()


app.add_api_route(**router.updates_route)
