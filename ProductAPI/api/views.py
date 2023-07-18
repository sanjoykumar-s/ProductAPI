from django.shortcuts import render
from rest_framework import generics
from .serializer import ProductSerializer
from .models import Product


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class =ProductSerializer