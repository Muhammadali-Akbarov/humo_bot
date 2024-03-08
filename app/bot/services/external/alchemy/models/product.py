"""
init sql alchemy model product
"""
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL, Text

from app.bot.services.external.alchemy import Base
from app.bot.services.external.alchemy import Session


class Product(Base):
    """
    product model
    """
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship("Category", back_populates="products")
    name = Column(String(255))
    price = Column(DECIMAL(10, 2))
    description = Column(Text)
    photo = Column(String(255))
    file_id = Column(String(255))


async def get_products(category_id):
    """
    get all products
    """
    session = Session()
    try:
        products = session.query(Product).filter_by(
            category_id=category_id
        ).all()
        return products

    finally:
        session.close()
