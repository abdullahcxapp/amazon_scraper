from rest_framework import serializers
from .models import Brand, Product


class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = ('id', 'name', 'details', 'amazon_url',
                  'created_at', 'updated_at', )


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name', 'asin', 'sku', 'image', 'brand',
                  'description', 'instructions', 'created_at',
                  'updated_at', )
