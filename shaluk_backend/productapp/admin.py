from django.contrib import admin
from . models import Product

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_id', 'product_name', 'product_description', 
                    'product_image', 'product_price']
    search_fields = ['product_name', 'product_description']
    list_filter = ['product_price']