"""
application controller abstraction
"""
import abc

from app.bot import models


class IAppController(abc.ABC):
    """
    application controller abstraction
    """
    async def create_or_update_client(self, client: models.Client):
        """
        create or update client interface
        """
        raise NotADirectoryError("create_or_update_client not implemented")
