from django.db.models import fields
from rest_framework import serializers
from ecomapp import models
from ecomapp.models import Product, Cart, CartProduct
from django.contrib.auth.models import User


class ProductSerializer(serializers.ModelSerializer):

    image_url = serializers.ReadOnlyField()

    class Meta:
        model = Product
        fields = '__all__'


class CartUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')


class CartProductSerializer(serializers.ModelSerializer):

    product_name = serializers.ReadOnlyField()
    product_price = serializers.ReadOnlyField()
    product_total = serializers.ReadOnlyField()
    product_image_url = serializers.ReadOnlyField()
    
    class Meta:
        model = CartProduct
        fields = (
            'product_name', 
            'product_price', 
            'product_total', 
            'product_image_url', 
            'quantity'
            )
        # fields = '__all__'


class CartSerializer(serializers.ModelSerializer):

    user = CartUserSerializer(read_only=True)
    cart_product = CartProductSerializer(read_only=True, many=True)
    cart_product_count = serializers.ReadOnlyField()
    cart_total_quantity = serializers.ReadOnlyField()
    cart_total_price = serializers.ReadOnlyField()

    class Meta:
        model = Cart
        fields = '__all__'