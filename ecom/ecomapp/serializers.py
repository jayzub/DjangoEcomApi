from django.db.models import fields
from rest_framework import serializers
from ecomapp import models
from ecomapp.models import Product, Cart
from django.contrib.auth.models import User


class ProductSerializer(serializers.ModelSerializer):

    image_url = serializers.ReadOnlyField()

    class Meta:
        model = Product
        fields = '__all__'


# class UserSerializer(serializers.ModelSerializer):
#     products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())

#     class Meta:
#         model = User
#         fields = '__all__'
#         # fields = (
#         #     'id',
#         #     'username',
#         #     'email',
#         #     'products',
#         # )


class CartUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')


class CartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'price', 'image_url')


class CartSerializer(serializers.ModelSerializer):

    user = CartUserSerializer(read_only=True)
    products = CartProductSerializer(read_only=True, many=True)

    class Meta:
        model = Cart
        fields = '__all__'