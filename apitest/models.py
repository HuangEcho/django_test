from django.db import models
# from product.models import Product


# Create your models here.
class ApiTest(models.Model):
    # django默认字段都是必填的。除非设置black=True
    # 如果是数字或者时间，要求 blank=True,null=True，才允许不设置；
    # blank=True不会改变数据库属性，不需要执行数据库命令；null=True会改变数据库属性，需要执行
    # 表单的必填 required=True; 非必填required=False
    product = models.ForeignKey("product.Product", on_delete=models.CASCADE, null=True)
    api_test_name = models.CharField("流程接口名称", max_length=64)
    # 设置description可以不填写
    api_test_desc = models.CharField("描述", max_length=64, null=True, blank=True)
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
    api_param_value = models.CharField("body", max_length=800)

    REQUEST_METHOD = (("get", "get"), ("post", "post"), ("put", "put"), ("delete", "delete"))
    api_method = models.CharField(verbose_name="请求方法", choices=REQUEST_METHOD, default="get", max_length=200, null=True)
    api_result = models.CharField("预期结果", max_length=800)
    # TODO: 这里可以考虑如何把响应结果存储在一个路径下，然后这里只放地址，就可以超链接过去
    api_response = models.CharField("响应数据", max_length=800, null=True, blank=True)
    api_status = models.BooleanField("是否通过")
    create_time = models.DateTimeField("创建时间", auto_now=True)

    def __str__(self):
        return self.api_name


class Apis(models.Model):
    product = models.ForeignKey("product.Product", on_delete=models.CASCADE, null=True)
    api_name = models.CharField("接口名称", max_length=100)
    api_url = models.CharField("url地址", max_length=200)
    api_param_value = models.CharField("请求参数和值", max_length=800)
    REQUEST_METHOD = (('0', 'get'), ('1', 'post'), ('2', 'put'), ('3', 'delete'), ('4', 'patch'))
    api_method = models.CharField(verbose_name="请求方法", choices=REQUEST_METHOD, default='0', max_length=200)
    api_result = models.CharField("预期结果", max_length=200)
    api_status = models.BooleanField("是否通过")
    create_time = models.DateTimeField("创建时间", auto_now=True)

    class Meta:
        verbose_name = "单一场景接口"
        verbose_name_plural = "单一场景接口"

    def __str__(self):
        return self.api_name
