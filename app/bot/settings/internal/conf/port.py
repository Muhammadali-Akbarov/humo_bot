"""
init port configuration
"""
from app.bot.settings.external.environs import env


SERVICE_ADDRESS = env.str("SERVICE_ADDRESS")
