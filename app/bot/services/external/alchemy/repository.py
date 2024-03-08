"""
the alchemy repository
"""
from app.bot.repositories import abstract
from app.bot.services.external.alchemy import models


class AlchemyRepository(abstract.IRepository):
    """
    the alchemy repository
    """
    async def create_or_update_client(self, client):
        await models.create_or_update_client(client)

    async def get_categories(self):
        return await models.get_categories()

    async def get_products(self, category_id):
        return await models.get_products(category_id)
