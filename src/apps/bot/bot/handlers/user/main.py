from aiogram import Router

from .start import start_router
from .callback.main import get_user_callback_router
from apps.bot.bot.middleware.collect_data import CollectData, CollectCallbackData

user_router = Router()

user_router.message.middleware(CollectData())
user_router.callback_query.middleware(CollectCallbackData())

def get_user_router() -> Router:
    user_routers = (start_router, get_user_callback_router(), )
    user_router.include_routers(*user_routers)

    return user_router
