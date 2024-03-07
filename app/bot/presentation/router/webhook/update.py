"""
the updates path
"""
from app.bot.presentation import handler


path = {
    "path": "/v1/humo/bot/webhook/",
    "endpoint": handler.webhook.updates_hander,
    "methods": [
        "POST"
    ]
}
