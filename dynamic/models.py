from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from services.FileServices import get_file_path

# Create your models here.
app_name = 'dynamic'


class Subdomain(models.Model):
    is_payment_done = models.BooleanField(default=False)
    sub_name = models.CharField(max_length=300)
    webinar = models.URLField(max_length=300)
    iphoneApp = models.URLField(max_length=300)
    androidApp = models.URLField(max_length=300)
    chromeExt = models.URLField(max_length=300)
    homeVideo = models.URLField(max_length=300)
    email = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phno = PhoneNumberField(blank=True)
    logo = models.ImageField(upload_to=get_file_path, blank=True)
    why_buy_link = models.CharField(max_length=200, blank=True)
    appImage = models.CharField(max_length=200, blank=True)
    primary_color = models.CharField(max_length=200, default='#115d22')
    secondary_color = models.CharField(max_length=200, default='#dee1e6')
    accent_color = models.CharField(max_length=200, default='#1c6ef9')
    bg_color = models.CharField(max_length=200, default='#f2f2f2')

    def __str__(self):
        return self.sub_name
