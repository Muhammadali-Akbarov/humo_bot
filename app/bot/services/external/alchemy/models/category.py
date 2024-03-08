"""
init sql alchemy category model
"""
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String

from app.bot.services.external.alchemy import Base
from app.bot.services.external.alchemy import Session


class Category(Base):
    """
    category model
    """
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    products = relationship("Product", back_populates="category")


async def get_categories():
    """
    get all categories
    """
    session = Session()
    try:
        categories = session.query(Category).all()
        return categories

    finally:
        session.close()
