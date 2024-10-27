from django.db import models


class BaseModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Brand(BaseModel):

    name = models.CharField(max_length=255)
    details = models.TextField(blank=True, null=True)
    amazon_url = models.URLField(max_length=500, unique=True)

    def __str__(self):
        return self.name


class Product(BaseModel):

    name = models.CharField(max_length=255)
    asin = models.CharField(max_length=30, blank=True, null=True)
    sku = models.CharField(max_length=50, blank=True, null=True)
    image = models.URLField(blank=True, null=True)
    brand = models.ForeignKey(Brand, related_name='products', on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    instructions = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
