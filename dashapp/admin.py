from django.contrib import admin
from dashapp.models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "sku")
    search_fields = ("name", "sku")