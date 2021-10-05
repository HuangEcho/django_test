from django.contrib import admin
from product.models import Product
from apitest.models import ApiTest, Apis

# Register your models here.


class ApisAdmin(admin.TabularInline):
    list_display = ["api_name", "api_url", "api_param_value", "api_method", "api_result", "api_status", "create_time",
                    "id", "product"]
    model = Apis
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ["product_name", "product_desc", "producer", "create_time", "id"]
    inlines = [ApisAdmin]


admin.site.register(Product)
