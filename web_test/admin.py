from django.contrib import admin
from web_test.models import WebCase, WebCaseStep


# Register your models here.
class WebCaseStepAdmin(admin.TabularInline):
    list_display = ["web_case_name", "web_case_step", "web_case_obj_name", "web_case_find_method", "web_case_element",
                    "web_case_opt_method", "web_cast_test_data", "web_case_assert_data", "web_case_result",
                    "create_time", "id", "web_case"]
    model = WebCaseStep
    extra = 1


class WebCaseAdmin(admin.ModelAdmin):
    list_display = ["web_case_name", "web_case_result", "create_time", "id", "product"]
    # model = WebCase
    # extra = 1
    inlines = [WebCaseStepAdmin]


class ProductAdmin(admin.ModelAdmin):
    list_display = ["product_name", "product_desc", "create_time", "id"]
    inlines = [WebCaseAdmin]


admin.site.register(WebCase, WebCaseAdmin)
