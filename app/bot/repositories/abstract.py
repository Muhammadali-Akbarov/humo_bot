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
