from django.db import models
from .product import Product
from .cart import Cart

class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_product')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return str(self.cart.user) + ':' + self.product.name

    def get_product_name(self):
        product_name = self.product.name
        return product_name
    product_name = property(get_product_name) 

    def get_product_image_url(self):
        product_image_url = self.product.image_url
        return product_image_url
    product_image_url = property(get_product_image_url) 

    def get_product_price(self):
        product_price = self.product.price
        return product_price
    product_price = property(get_product_price) 

    def get_product_total(self):
        total = self.product.price * self.quantity
        return total
    product_total = property(get_product_total)   