from django.db import models

# Create your models here.
from django.db import models


class Device(models.Model):
    name = models.CharField(max_length=20)
    device_tag = models.CharField(max_length=10, unique=True)
    price = models.FloatField(default=100)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=20)
    phone_number= models.CharField(max_length= 20, unique=True)

    def __str__(self):
        return self.name

class History(models.Model):
    customer = models.CharField(max_length = 20)
    device = models.CharField(max_length=20)
    units = models.IntegerField(default=0)
    price = models.FloatField(default=100)

    def __str__(self):
        return self.customer + self.device
