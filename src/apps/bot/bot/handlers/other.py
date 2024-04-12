from aiogram import types, Router
from aiogram.types import Message, CallbackQuery

from apps.bot.bot.middleware.collect_data import CollectData, CollectCallbackData

other_router = Router()

other_router.message.middleware(CollectData())
other_router.callback_query.middleware(CollectCallbackData())


@other_router.message()
async def handle_other_messages(message: Message):
    pass


@other_router.callback_query()
async def handle_other_callback(query: CallbackQuery):
    pass
