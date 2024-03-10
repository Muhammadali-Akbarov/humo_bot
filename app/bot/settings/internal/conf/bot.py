"""
the entry point model
"""
from app.bot.settings.external.environs import env

IS_WEBHOOK_ENABLED = env.bool("IS_WEBHOOK_ENABLED", False)

# pylint: disable=C0103
url = env.str("ENTRYPOINT_URL")
entrypoint_image = env.str("ENTRYPOINT_IMAGE")
extrypoint_phone_number = env.str("ENTRYPOINT_PHONE_NUMBER")

entrypoint_description = f"""
<b><a href="{url}">Humo savdo</a></b>

Bizda barcha turdagi maishiy texnika vositalari arzon narxlarda sizni kutmoqda. Tashrif buyuring va o'zingiz uchun qulay narxlarda xarid qiling.

Murojat uchun:  ☎️ <a href="tel:{extrypoint_phone_number}">{extrypoint_phone_number}</a>
""" # noqa
