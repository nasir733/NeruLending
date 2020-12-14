from django.core.validators import MinValueValidator
from django.db import models

from dynamic.models import Subdomain
from services.StripeService import StripeService


class BusinessTierModel(models.Model):
    class Meta:
        abstract = True

    company_name = models.CharField(max_length=500, null=True)
    product = models.CharField(max_length=500, null=True)
    tradeline_amount = models.CharField(max_length=500, null=True)
    tradeline_credit_amount = models.CharField(max_length=500, null=True)
    company_reports_to = models.CharField(max_length=500, null=True)
    we_can_help = models.BooleanField(null=True, default=True)
    recommended = models.TextField(null=True, blank=True)
    tier = models.CharField(max_length=10, null=True, blank=True)

    price = models.DecimalField(max_digits=100, default=0, decimal_places=2, validators=[MinValueValidator(0)])
    charge = models.DecimalField(max_digits=100, default=0, decimal_places=2, validators=[MinValueValidator(0)])

    whitelabel_portal = models.ForeignKey(Subdomain, on_delete=models.CASCADE, null=True, blank=True)

    product_id = models.CharField(max_length=100, null=True, blank=True)
    price_id = models.CharField(max_length=100, null=True, blank=True)
    price_lookup = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.company_name} {self.product} tradeline"

    def save(self, *args, **kwargs):
        if self.price < 0 or self.charge < 0:
            return

        if not self.product_id:
            response = StripeService.create_product(str(self), float(self.price) + float(self.charge),
                                                    self.company_name)
            self.product_id = response['prod_id']
            self.price_id = response['price_id']
            self.price_lookup = response['price_lookup']
        else:
            price_id, _ = StripeService.update_product(self.product_id, self.price_id, str(self),
                                                       float(self.price) + float(self.charge))
            if price_id != self.price_id:
                self.price_id = price_id
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        StripeService.delete_product(self.product_id)
        super().delete(*args, **kwargs)


class TimeTrackedModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    @property
    def get_url(self):
        if hasattr(self, 'url'):
            if not self.url.startswith("http"):
                return "http://" + self.url
            else:
                return self.url


class ProductModel(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(max_length=500, default='Product', null=True)

    price = models.DecimalField(max_digits=100, default=0, decimal_places=2, validators=[MinValueValidator(0)])
    charge = models.DecimalField(max_digits=100, default=0, decimal_places=2, validators=[MinValueValidator(0)])

    whitelabel_portal = models.ForeignKey(Subdomain, on_delete=models.CASCADE, null=True, blank=True)

    product_id = models.CharField(max_length=100, null=True, blank=True)
    price_id = models.CharField(max_length=100, null=True, blank=True)
    price_lookup = models.CharField(max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.price < 0 or self.charge < 0:
            return

        if not self.product_id:
            response = StripeService.create_product(str(self), float(self.price) + float(self.charge), self.name)
            self.product_id = response['prod_id']
            self.price_id = response['price_id']
            self.price_lookup = response['price_lookup']
        else:
            price_id, _ = StripeService.update_product(self.product_id, self.price_id, str(self),
                                                       float(self.price) + float(self.charge))
            if price_id != self.price_id:
                self.price_id = price_id
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        StripeService.delete_product(self.product_id)
        super().delete(*args, **kwargs)
