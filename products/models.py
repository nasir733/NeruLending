import os
import uuid

from django.conf import settings
from django.db import models
from django.utils.safestring import mark_safe
from user.models import Profile


class tradelines(models.Model):
    company_name = models.CharField(max_length=200)
    product = models.CharField(max_length=200)
    tradeline_amount = models.IntegerField()
    company_reports_to = models.CharField(max_length=200)
    cost = models.IntegerField()
    video_link = models.URLField(max_length=300)

    def __str__(self):
        return self.company_name

