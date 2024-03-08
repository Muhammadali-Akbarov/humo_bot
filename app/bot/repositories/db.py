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


repository = Repository(AlchemyRepository())
