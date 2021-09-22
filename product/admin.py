from django.contrib import admin
from product.models import Product

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ["product_name", "product_desc", "producer", "create_time", "id"]

    admin.site.register(Product)
