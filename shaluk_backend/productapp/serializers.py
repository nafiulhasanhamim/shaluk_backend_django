# product/serializers.py
from rest_framework import serializers
from .models import Product
from shopapp.serializers import ShopSerializer 

class ProductSerializer(serializers.ModelSerializer):
    shop = ShopSerializer()
    class Meta:
        model = Product
        fields = '__all__'


