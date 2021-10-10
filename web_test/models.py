from django.db import models
# from product.models import Product


# Create your models here.
class WebCase(models.Model):
    product = models.ForeignKey("product.Product", on_delete=models.CASCADE, null=True)
    web_case_name = models.CharField("用例名称", max_length=200)
    web_case_result = models.BooleanField("测试结果")
    web_tester = models.CharField("测试负责人", max_length=200)
    create_time = models.DateTimeField("创建时间", auto_now=True)

    class Meta:
        verbose_name = "web测试用例"
        verbose_name_plural = "web测试用例"

    def __str__(self):
        return self.web_case_name


class WebCaseStep(models.Model):
    web_case = models.ForeignKey("WebCase", on_delete=models.CASCADE)
    web_case_name = models.CharField("web测试用例名称", max_length=200)
    web_case_step = models.CharField("web测试用例步骤", max_length=200)
    web_case_obj_name = models.CharField("web测试对象名称", max_length=200)
    web_case_find_method = models.CharField("定位方式", max_length=200)
    web_case_element = models.CharField("控件元素", max_length=200)
    web_case_opt_method = models.CharField("操作方法", max_length=200)
    web_case_test_data = models.CharField("测试数据", max_length=200)
    web_case_assert_data = models.CharField("验证数据", max_length=200)
    web_case_result = models.CharField("测试结果", max_length=200)
    create_time = models.DateTimeField("创建时间", auto_now=True)

    def __str__(self):
        return self.web_case_name
