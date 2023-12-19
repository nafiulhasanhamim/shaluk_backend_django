import uuid
from django.db import models

# Create your models here.
class Shop(models.Model):
    shop_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    shop_name = models.CharField(max_length=100)
    shop_address = models.CharField(max_length=100)
    shop_type = models.CharField(max_length=100)
    shop_number = models.CharField(max_length=13)

    def __str__(self):
        return self.shop_name
    
    