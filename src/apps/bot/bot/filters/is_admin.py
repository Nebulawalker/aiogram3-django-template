from aiogram.filters import BaseFilter
from aiogram.types import Message, CallbackQuery

from django.conf import settings


class OnlyAdmin(BaseFilter):
    async def __call__(self, message: Message, *args, **kwargs):
        for admin_id in settings.ADMINS_ID:
            if message.from_user.id == admin_id:
                return True

        return False


class OnlyAdminCallback(BaseFilter):
    async def __call__(self, query: CallbackQuery, *args, **kwargs):
        for admin_id in settings.ADMINS_ID:
            if query.from_user.id == admin_id:
                return True

        return False
