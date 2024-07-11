from django.db import models
from django.contrib.auth.models import User
from products.models import Product
# Create your models here.

class shopcart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(default=1)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, blank=True,null=True)

    def save(self, *args, **kwargs):
        self.subtotal = (self.product.new_price) * self.qty
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.product.name}'