from django.shortcuts import render
from rest_framework import generics, permissions
from ecomapp.models import Product, Cart
from ecomapp.serializers import ProductSerializer, CartSerializer


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


class CartListView(generics.ListAPIView):
    """
    Returns list of all Carts
    """
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]


class CreateCartView(generics.CreateAPIView):
    """
    Create a new Cart
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CartSerializer


class UpdateCartView(generics.UpdateAPIView):
    """
    Update a selected Cart
    """
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'
    queryset = Cart.objects.all()

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class DeleteProductView(generics.DestroyAPIView):
    """
    Remove a selected Cart
    """
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'
    queryset = Cart.objects.all()