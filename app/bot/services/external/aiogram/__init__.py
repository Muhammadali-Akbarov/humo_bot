"""
start handler
"""
import aiogram
from app.bot.settings.external.aiogram import conf


bot = aiogram.Bot(**conf.bot)
dispatcher = aiogram.Dispatcher()
