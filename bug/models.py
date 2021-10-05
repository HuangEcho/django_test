from django.db import models
from product.models import Product


# Create your models here.
class Bug(models.Model):
    Product = models.ForeignKey("product.Product", on_delete=models.CASCADE, null=True)
    bug_name = models.CharField("bug name", max_length=64)
    bug_detail = models.CharField("bug detail", max_length=200)

    BUG_STATUS = (("激活", "激活"), ("已解决", "已解决"), ("已关闭", "已关闭"))
    bug_status = models.CharField("解决状态", choices=BUG_STATUS, default="激活", max_length=200, null=True)

    BUG_LEVEL = [("1", "1"), ("2", "2"), ("3", "3")]
    bug_level = models.CharField("bug等级", choices=BUG_LEVEL, default="3", max_length=200, null=True)

    bug_creator = models.CharField("创建人", max_length=200)
    bug_assign = models.CharField("分配给", max_length=200)
    create_time = models.DateTimeField("创建时间", auto_now=True)

    class Meta:
        verbose_name = "bug管理"
        verbose_name_plural = "bug管理"

    def __str__(self):
        return self.bug_name

