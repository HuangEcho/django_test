from django.contrib import admin
from apitest.models import ApiTest, ApiStep


# Register your models here.
class ApiStepAdmin(admin.TabularInline):
    list_display = ["api_name", "api_url", "api_param_value", "api_method", "api_result", "api_status", "create_time",
                    "id", "api_test"]
    model = ApiStep
    extra = 1


class ApiTestAdmin(admin.TabularInline):
    list_display = ["api_test_name", "api_tester", "api_test_result", "create_time", "id"]
    inlines = [ApiStepAdmin]


admin.site.register(ApiTest)
