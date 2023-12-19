from django.contrib import admin
from . models import Shop

# Register your models here.
@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['shop_id', 'shop_name', 'shop_type', 
                    'shop_address', 'shop_number']
    search_fields = ['shop_name', 'shop_address', 'shop_number']
    list_filter = ['shop_type']