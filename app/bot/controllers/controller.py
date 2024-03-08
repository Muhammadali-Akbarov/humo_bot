"""
implementation of controller interface
"""
from app.bot import models
from app.bot import repositories

from app.bot.controllers import IAppController


class AppController(IAppController):
    """
    implementation of controller interface
    """
    def __init__(
        self,
        repository: repositories.IRepository,
    ):
        self.repository = repository

    async def create_or_update_client(
        self,
        client: models.Client
    ) -> models.Client | None:
        await self.repository.create_or_update_client(client)

    async def get_categories(self) -> list[models.Category]:
        return await self.repository.get_categories()

    async def get_products(self, category_id) -> list[models.Product]:
        return await self.repository.get_products(
            category_id=category_id
        )


controller = AppController(
    repository=repositories.repository
)
