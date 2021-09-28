from django.db import models
from product.models import Product


# Create your models here.
class ApiTest(models.Model):
    Product = models.ForeignKey("product.Product", on_delete=models.CASCADE, null=True)
    api_test_name = models.CharField("流程接口名称", max_length=64)
    api_test_desc = models.CharField("描述", max_length=64, null=True)
    api_tester = models.CharField("测试负责人", max_length=16)
    api_test_result = models.BooleanField("测试结果")
    create_time = models.DateTimeField("创建时间", auto_now=True)

    class Meta:
        verbose_name = "流程场景接口"
        verbose_name_plural = "流程场景接口"

    def __str__(self):
        return self.api_test_name


class ApiStep(models.Model):
    api_test = models.ForeignKey(ApiTest, on_delete=models.CASCADE)
    api_name = models.CharField("接口名称", max_length=100)
    api_url = models.CharField("url地址", max_length=200)
    api_step = models.CharField("测试步骤", max_length=100, null=True)
    api_param_value = models.CharField("请求参数和值", max_length=800)

    REQUEST_METHOD = (("get", "get"), ("post", "post"), ("put", "put"), ("delete", "delete"), ("patch", "patch"))
    api_method = models.CharField(verbose_name="请求方法", choices=REQUEST_METHOD, default="get", max_length=200, null=True)
    api_result = models.CharField("预期结果", max_length=200)
    api_response = models.CharField("响应数据", max_length=5000, null=True)
    api_status = models.BooleanField("是否通过")
    create_time = models.DateTimeField("创建时间", auto_now=True)

    def __str__(self):
        return self.api_name
