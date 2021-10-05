from django.contrib import admin
from settings.models import Settings


# Register your models here.
class SettingsAdmin(admin.ModelAdmin):
    list_display = {"settings_name", "settings_value", "id"}


# 注册models的类
admin.site.register(Settings)
