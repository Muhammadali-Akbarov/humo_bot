"""
the category shortcuts
"""
from app.bot.controllers import controller
from app.bot.services.external.aiogram import shortcut


async def get_category_actions():
    """
    get category actions
    """
    actions = []
    categories = await controller.get_categories()

    for category in categories:
        actions.append({
            "text": category.name,
            "callback_data": str(category.id)
        })

    schema = shortcut.get_schema(len(categories))

    return {
        "actions": actions,
        "schema": schema
    }
