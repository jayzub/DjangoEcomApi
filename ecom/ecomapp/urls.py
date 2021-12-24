from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='index'),
    path('create_product/', views.CreateProductView.as_view(), name='create_product'),
    path('list_products/', views.ProductListView.as_view(), name='list_products'),
    path('update_product/<int:id>/', views.UpdateProductView.as_view(), name='update_product'),
    path('delete_product/<int:id>/', views.DeleteProductView.as_view(), name='delete_product'),

    path('create_cart/', views.CreateCartView.as_view(), name='create_cart'),
    path('list_carts/', views.CartListView.as_view(), name='list_carts'),
    path('update_cart/<int:id>/', views.UpdateCartView.as_view(), name='update_cart'),
    path('delete_cart/<int:id>/', views.DeleteProductView.as_view(), name='delete_cart'),
]