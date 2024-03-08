"""
the alchemy repository
"""
from app.bot.repositories import abstract
from app.bot.services.external.alchemy import model


class AlchemyRepository(abstract.IRepository):
    """
    the alchemy repository
    """
    async def create_or_update_client(self, client):
        await model.create_or_update_client(client)
