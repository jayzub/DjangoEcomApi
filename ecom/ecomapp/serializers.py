from rest_framework import serializers
from ecomapp.models import Product


class ProductSerializer(serializers.ModelSerializer):

    img_url = serializers.ReadOnlyField()

    class Meta:
        model = Product
        fields = '__all__'