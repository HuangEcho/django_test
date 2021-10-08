from django.contrib import admin
from settings.models import Settings


# Register your models here.
class SettingsAdmin(admin.ModelAdmin):
    list_display = {"setting_name", "setting_value", "id"}


# 注册models的类
admin.site.register(Settings)
