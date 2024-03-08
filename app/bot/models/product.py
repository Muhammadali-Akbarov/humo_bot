"""
the product model
"""
from typing import Optional
from pydantic import BaseModel


class Product(BaseModel):
    """
    pydantic base model for Product
    """
    category_id: int
    name: str
    price: float
    description: str
    photo: str
    file_id: Optional[str]
