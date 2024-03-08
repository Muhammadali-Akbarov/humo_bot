"""
init repository layer
"""
from app.bot.repositories import abstract
from app.bot.services.external.alchemy.repository import AlchemyRepository


class Repository(abstract.IRepository):
    """
    repository layer implementation
    """
    def __init__(self, repo: abstract.IRepository):
        self.repository = repo

    async def create_or_update_client(self, client) -> None:
        return await self.repository.create_or_update_client(client=client)

    async def get_categories(self):
        return await self.repository.get_categories()

    async def get_products(self, category_id):
        return await self.repository.get_products(
            category_id=category_id
        )


repository = Repository(AlchemyRepository())
