# product/serializers.py
from rest_framework import serializers
from .models import Order
from productapp.serializers import ProductSerializer
from user.serializers import UserSerializer

class OrderSerializer(serializers.ModelSerializer):

    # if I dont want to use depth then use this..works same
    # product = ProductSerializer()
    # user = UserSerializer()
    
    class Meta:
        model = Order
        fields = '__all__'
        # depth = 2

class UserOrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = Order
        fields = '__all__'


