from django.shortcuts import render
from rest_framework import generics, permissions
from ecomapp.models import Product
from ecomapp.serializers import ProductSerializer


class ProductListView(generics.ListAPIView):
    """
    Returns list of all Products
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]


class CreateProductView(generics.CreateAPIView):
    """
    Create a new Product
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProductSerializer


class UpdateProductView(generics.UpdateAPIView):
    """
    Update a selected Product
    """
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'
    queryset = Product.objects.all()

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class DeleteProductView(generics.DestroyAPIView):
    """
    Remove a selected Product
    """
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'
    queryset = Product.objects.all()
