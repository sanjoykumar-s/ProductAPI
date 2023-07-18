from django.contrib import admin
from django.urls import path
from .views import ProductList, ProductDetail

urlpatterns = [
    path('product/',ProductList.as_view(), name = 'product-list'),
    path('product/<int:pk>/',ProductDetail.as_view(), name='product-detail'),
]
