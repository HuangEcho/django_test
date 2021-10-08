from django.contrib import admin
from app_test.models import AppCase, AppCaseStep


# Register your models here.
class AppCaseStepAdmin(admin.TabularInline):
    list_display = ["app_case_step", "app_case_object_name", "app_case_find_method", "app_case_element",
                    "app_case_op_method", "app_case_assert_data", "app_case_result", "create_time", "id",
                    "app_case"]
    model = AppCaseStep
    extra = 1


class AppCaseAdmin(admin.ModelAdmin):
    list_display = ["app_case_name", "app_case_result", "create_time", "id"]
    inlines = [AppCaseStepAdmin]


admin.site.register(AppCase, AppCaseAdmin)
