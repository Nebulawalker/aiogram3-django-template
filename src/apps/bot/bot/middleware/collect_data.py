from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

from apps.bot.models import User


class CollectData(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ) -> Any:
        user = await User.objects.aupdate_or_create(
            telegram_id=event.from_user.id,
            username=event.from_user.username,
            defaults={
                'first_name': event.from_user.first_name,
                'last_name': event.from_user.last_name,
                'is_premium': event.from_user.is_premium,
            }
        )
        data.update({
            'user': user
        })
        result = await handler(event, data)
        return result


class CollectCallbackData(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ) -> Any:
        user = await User.objects.aupdate_or_create(
            telegram_id=event.from_user.id,
            username=event.from_user.username,
            defaults={
                'first_name': event.from_user.first_name,
                'last_name': event.from_user.last_name,
                'is_premium': event.from_user.is_premium,
            }
        )
        data.update({
            'user': user
        })
        result = await handler(event, data)
        return result
