"""
the category model
"""
from pydantic import BaseModel


class Category(BaseModel):
    """
    pydantic base model for Category
    """
    id: int
    name: str
