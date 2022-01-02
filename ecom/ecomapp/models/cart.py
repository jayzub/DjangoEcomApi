from django.db import models
from django.contrib.auth.models import User


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)    

    def __str__(self):
        return f'{self.user}'


    def get_cart_product_count(self):
        cartproducts = self.cart_product.all()
        product_count = len([product for product in cartproducts])
        return product_count
    cart_product_count = property(get_cart_product_count)


    def get_cart_total_quantity(self):
        cartproducts = self.cart_product.all()
        total = sum([product.quantity for product in cartproducts])
        return total
    cart_total_quantity = property(get_cart_total_quantity)


    def get_cart_total_price(self):
        cartproducts = self.cart_product.all()
        total = sum([product.product_total for product in cartproducts])
        return total
    cart_total_price = property(get_cart_total_price)