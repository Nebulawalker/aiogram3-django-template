from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import User, UserLogs


# Register your models here.

class UserLogsTabular(admin.TabularInline):
    model = UserLogs

    def has_add_permission(self, request, obj):
        return True


class BotUsers(admin.ModelAdmin):
    @mark_safe
    def display_username_link(self, obj):
        return f'<a href="https://t.me/{obj.username}" target="_blank">{obj.username}</a> ' if obj.username else 'Нету'

    inlines = (UserLogsTabular,)

    display_username_link.short_description = 'Ссылка на пользователя'

    list_display = (
    'telegram_id', 'display_username_link', 'first_name', 'last_name', 'is_premium', 'registration_date',
    'last_activity')
    fields = (
    'telegram_id', 'username', 'display_username_link', 'first_name', 'last_name', 'is_premium', 'registration_date',
    'last_activity')
    readonly_fields = ('registration_date', 'last_activity', 'display_username_link')


admin.site.register(User, BotUsers)
