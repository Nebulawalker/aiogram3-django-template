from aiogram import types, Router

from apps.bot.bot.middleware.collect_data import CollectData, CollectCallbackData

other_router = Router()

other_router.message.middleware(CollectData())
other_router.callback_query.middleware(CollectCallbackData())