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
