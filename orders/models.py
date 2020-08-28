import os
import uuid

from django.conf import settings
from django.db import models
from django.utils.safestring import mark_safe
from user.models import Profile
from products.models import tradelines



class TradelineOrder(models.Model):
    user =  models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    tradeline=models.ForeignKey(
        tradelines,
        on_delete=models.CASCADE,
    )
    
