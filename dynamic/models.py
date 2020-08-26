from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
app_name = 'dynamic'


class subdomain(models.Model):
    sub_name = models.CharField(max_length=300)
    webinar = models.URLField(max_length=300)
    iphoneApp = models.URLField(max_length=300)
    androidApp = models.URLField(max_length=300)
    chromeExt = models.URLField(max_length=300)
    homeVideo = models.URLField(max_length=300)
    email = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phno = models.CharField(max_length=200, blank=True)
    fav_icon = models.ImageField(upload_to='media', blank=True)

    def __str__(self):
        return self.sub_name
