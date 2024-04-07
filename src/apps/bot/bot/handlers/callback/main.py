from aiogram import Router

from .start import start_callback_router
from apps.bot.bot.middleware.collect_data import CollectCallbackData

other_callback_router = Router()

other_callback_router.callback_query.middleware(CollectCallbackData())


def get_other_callback_router() -> Router:
    other_callback_routers = (start_callback_router,)
    other_callback_router.include_routers(*other_callback_routers)

    return other_callback_router
