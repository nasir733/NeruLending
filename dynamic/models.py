from django.db import models

# Create your models here.
app_name= 'dynamic'

class subdomain(models.Model):
    sub_name=models.CharField(max_length=300)
    webinar= models.URLField(max_length=300)
    iphoneApp= models.URLField(max_length=300)
    androidApp= models.URLField(max_length=300)
    chromeExt= models.URLField(max_length=300)
    homeVideo= models.URLField(max_length=300)

    def __str__(self):
        return self.sub_name
