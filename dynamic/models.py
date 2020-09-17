from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from services.FileServices import get_file_path
from user.models import Profile

app_name = 'dynamic'


class Subdomain(models.Model):
    is_payment_done = models.BooleanField(default=False)
    sub_name = models.CharField(max_length=300)
    webinar = models.URLField(max_length=300)
    iphoneApp = models.URLField(max_length=300)
    androidApp = models.URLField(max_length=300)
    chromeExt = models.URLField(max_length=300)
    homeVideo = models.URLField(max_length=300)
    extensionVideo = models.URLField(max_length=300)
    email = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phno = PhoneNumberField(blank=True)
    logo = models.ImageField(upload_to=get_file_path)
    why_buy_link = models.CharField(max_length=200, blank=True)
    appImage = models.CharField(max_length=200, blank=True)
    primary_color = models.CharField(max_length=200, blank=True)
    secondary_color = models.CharField(max_length=200, blank=True)
    accent_color = models.CharField(max_length=200, blank=True)
    bg_color = models.CharField(max_length=200, blank=True)

    admins = models.ManyToManyField(Profile, related_name='portals')

    def __str__(self):
        return self.sub_name
