import datetime
from django.db import models

# Create your models here.
class user(models.Model):
    objects = None
    product_name = models.CharField(max_length=70)
    quantity = models.IntegerField()
    customer_number = models.IntegerField(max_length=30)
    purshasing_price = models.IntegerField()
    date = models.DateTimeField(default=datetime.datetime.now())
