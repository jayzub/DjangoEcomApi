from django.db import models
from django.contrib.auth.models import User

from .product import Product

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product)

    class Meta:
        ordering = ['user', '-date_created']

    # product (many to many)
        # quantity
        # total_price (property)
        # cart_total_quantity (property)
        # cart_total_price (property)
    

    def __str__(self):
        return f'{self.user}'