from django.conf import settings
from django.db import models

# Create your models here.
from core.models import ProductModel


class Product(ProductModel):
    description = models.TextField(null=True)
    video = models.URLField(null=True)


class ProductPurchasedModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    payments_left = models.DecimalField(max_digits=100, default=0, decimal_places=2)
    amount_left = models.DecimalField(max_digits=100, default=0, decimal_places=2)
