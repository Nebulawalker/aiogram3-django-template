from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from django.conf import settings

from apps.bot.bot.handlers.main import get_all_routers

dp = Dispatcher()


async def start_bot():
    dp.include_routers(*get_all_routers())
    bot = Bot(token=settings.BOT_TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)
