"""
init sql alchemy client model
"""
from sqlalchemy import Column, BigInteger, String

from app.bot import models
from app.bot.services.external.alchemy import Base
from app.bot.services.external.alchemy import Session


class Client(Base):
    """
    client model
    """
    __tablename__ = 'client'

    id = Column(BigInteger, primary_key=True)
    username = Column(String)
    first_name = Column(String)
    last_name = Column(String)


async def create_or_update_client(
    client: models.Client,
):
    """
    function to create or update a client in the database
    """
    with Session() as session:
        user = session.query(Client).filter_by(
            username=client.username
        ).first()

        if user:
            user.first_name = client.first_name
            user.last_name = client.last_name

        if not user:
            user = Client(
                id=client.chat_id,
                username=client.username,
                first_name=client.first_name,
                last_name=client.last_name
            )
            session.add(user)

        session.commit()
