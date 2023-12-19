from django.contrib import admin
from . models import Order

# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'product', 'quantity', 'total_price', 'user', 'order_status']
    search_fields = ['order_id', 'product__product_name', 'user__username']
    list_filter =['order_status']