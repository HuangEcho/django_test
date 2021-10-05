from django.contrib import admin
from apitest.models import ApiTest, ApiStep, Apis
from product.models import Product


# Register your models here.
class ApiStepAdmin(admin.TabularInline):
    list_display = ["api_name", "api_url", "api_param_value", "api_method", "api_result", "api_status", "create_time",
                    "id", "api_test"]
    model = ApiStep
    extra = 1


# 这里要记成admin.ModelAdmin, 在admin.site.register里才能注册
class ApiTestAdmin(admin.ModelAdmin):
    list_display = ["api_test_name", "api_tester", "api_test_result", "create_time", "id"]
    inlines = [ApiStepAdmin]


admin.site.register(ApiTest, ApiTestAdmin)


class ApisAdmin(admin.TabularInline):
    list_display = ["api_name", "api_url", "api_param_value", "api_method", "api_result", "api_status", "create_time",
                    "id", "product"]


admin.site.register(Apis)
