"""
init repository abstraction
"""
import abc

from app.bot import models


class IRepository(abc.ABC):
    """
    repository abstraction
    """
    @abc.abstractmethod
    async def create_or_update_client(
        self,
        client: models.Client,
    ) -> None:
        """
        create or update user
        """
        raise NotImplementedError("create_or_update_user not implemented!")

    @abc.abstractmethod
    async def get_categories(self):
        """
        get all categories
        """
        raise NotImplementedError("get_categories not implemented!")

    @abc.abstractmethod
    async def get_products(self, category_id):
        """
        get all products
        """
        raise NotImplementedError("get_products not implemented!")
