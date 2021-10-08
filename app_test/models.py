from django.db import models


# Create your models here.
class AppCase(models.Model):
    Product = models.ForeignKey("product.Product", on_delete=models.CASCADE, null=True)
    app_case_name = models.CharField("用例名称", max_length=200)
    app_case_result = models.BooleanField("测试结果")
    app_case_tester = models.CharField("测试负责人", max_length=16)
    create_time = models.DateTimeField("创建时间", auto_now=True)

    class Meta:
        verbose_name = "app测试用例"
        verbose_name_plural = "app测试用例"

    def __str__(self):
        return self.app_case_name


class AppCaseStep(models.Model):
    app_case = models.ForeignKey("AppCase", on_delete=models.CASCADE)
    app_case_step = models.CharField("测试步骤", max_length=200)
    app_case_object_name = models.CharField("测试对象名称描述", max_length=200)
    app_case_find_method = models.CharField("定位方式", max_length=200)
    app_case_element = models.CharField("控件元素", max_length=200)
    app_case_op_method = models.CharField("操作方法", max_length=200)
    app_case_test_data = models.CharField("测试数据", max_length=200, null=True, blank=True)
    app_case_assert_data = models.CharField("验证数据", max_length=200)
    app_case_result = models.BooleanField("测试结果")
    creat_time = models.DateTimeField("创建时间", auto_now=True)

    def __str__(self):
        return self.app_case_step

