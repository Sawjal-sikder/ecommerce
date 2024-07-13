from django.db import models


# Create your models here.
class Product(models.Model):  # Class names should be capitalized
    name = models.CharField(max_length=55)
    color = models.CharField(max_length=25)
    sku = models.CharField(max_length=25)
    price = models.FloatField()

    def __str__(self):
        return self.name
