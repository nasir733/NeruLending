from django.conf import settings
from django.db import models

from products.models import Tradelines
from user.models import Profile


class TradelineOrder(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tradeline = models.ForeignKey(Tradelines, on_delete=models.CASCADE)
