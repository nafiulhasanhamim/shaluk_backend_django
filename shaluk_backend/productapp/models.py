# product/models.py
import uuid
from django.db import models
from shopapp.models import Shop

class Product(models.Model):
    product_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_name = models.CharField(max_length=255)
    product_description = models.TextField()
    product_image = models.URLField()
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.product_name


