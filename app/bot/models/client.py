"""
the client initalizes
"""
import typing
from pydantic import BaseModel


class Client(BaseModel):
    """
    pydantic base model for User
    """
    chat_id: int
    username: str
    first_name: str
    last_name: typing.Optional[str]


async def build_client(message):
    """
    builds a client
    """
    return Client(
        chat_id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name
    )
