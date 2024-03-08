"""
application controller abstraction
"""
import abc

from app.bot import models


class IAppController(abc.ABC):
    """
    application controller abstraction
    """
    async def create_or_update_client(
        self,
        client: models.Client
    ) -> models.Client | None:
        """
        create or update client interface
        """
        raise NotADirectoryError("create_or_update_client not implemented")

    async def get_categories(self) -> list[models.Category]:
        """
        get categories interface
        """
        raise NotADirectoryError("get_categories not implemented")

    async def get_products(self, category_id):
        """
        get products interface
        """
        raise NotADirectoryError("get_products not implemented")
