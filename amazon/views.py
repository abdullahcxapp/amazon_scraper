from rest_framework import generics

from .models import Brand, Product
from .serializer import BrandSerializer, ProductSerializer


class BrandListAPIView(generics.ListCreateAPIView):

    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class ProductListAPIView(generics.ListCreateAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
