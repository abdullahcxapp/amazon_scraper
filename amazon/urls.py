from django.urls import path
from .views import BrandListAPIView, ProductListAPIView


urlpatterns = [
    path('brands/', BrandListAPIView.as_view(), name='brand-list'),
    path('products/', ProductListAPIView.as_view(), name='product-list'),
]
