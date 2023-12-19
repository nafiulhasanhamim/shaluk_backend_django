import uuid
from django.db import models
from productapp.models import Product
# from authapp.models import Users
from user.models import User
from django.contrib.auth import get_user_model

class Order(models.Model):
    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders', db_column='product_id')
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    # user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='orders', db_column='user_id')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders', db_column='user_id')
    order_status = models.CharField(max_length=255)

    def __str__(self):
        return f"Order {self.order_id}"
