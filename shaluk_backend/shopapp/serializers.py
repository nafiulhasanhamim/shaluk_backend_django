from rest_framework import serializers
from . models import Shop
 
#model serializer
class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ['shop_id', 'shop_name', 'shop_type', 
                    'shop_address', 'shop_number']
        read_only_fields = ['shop_id']



