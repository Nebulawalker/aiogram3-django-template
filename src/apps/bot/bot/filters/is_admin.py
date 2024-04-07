from aiogram.filters import BaseFilter
from aiogram.types import Message, CallbackQuery

from django.conf import settings


class OnlyAdmin(BaseFilter):
    async def __call__(self, message: Message, *args, **kwargs):
        if str(message.from_user.id) in settings.ADMINS_ID:
            return True

        return False


class OnlyAdminCallback(BaseFilter):
    async def __call__(self, query: CallbackQuery, *args, **kwargs):
        if str(query.message.from_user.id) in settings.ADMINS_ID:
            return True

        return False
