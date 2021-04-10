from django.db import models

# Create your models here.
from django.db import models


class Device(models.Model):
    name = models.CharField(max_length=20)
    device_tag = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

