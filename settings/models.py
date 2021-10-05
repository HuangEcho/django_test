from django.db import models


# Create your models here.
class Settings(models.Model):
    settings_name = models.CharField("设置名称", max_length=200)
    settings_value = models.CharField("设置参数", max_length=200)

    class Meta:
        verbose_name = "系统设置"
        verbose_name_plural = "系统设置"

    def __str__(self):
        return self.settings_name
