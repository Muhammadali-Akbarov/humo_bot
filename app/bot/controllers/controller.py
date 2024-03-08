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

    async def create_or_update_client(self, client: models.Client):
        await self.repository.create_or_update_client(client)


controller = AppController(
    repository=repositories.repository
)
