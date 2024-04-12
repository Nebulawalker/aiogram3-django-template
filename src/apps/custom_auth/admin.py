from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from .models import CustomUser, CustomGroup


# Register your models here.


admin.site.unregister(Group)
admin.site.register(CustomUser, BaseUserAdmin)
admin.site.register(CustomGroup)
