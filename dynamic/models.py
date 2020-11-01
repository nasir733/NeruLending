from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from products.services import create_usersteps_for_subdomain, create_tradelines_for_subdomain
from services.FileServices import get_file_path
from services.HostsService import HostsService
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
    faq_page = models.CharField(max_length=300, null=True,
                                default='https://businessbuilders.zendesk.com/hc/en-us/sections/360010349512-FAQ')
    creditRepairLink = models.CharField(max_length=300, null=True, default='/business/credit-affiliate')
    email = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phno = PhoneNumberField(blank=True)
    logo = models.ImageField(upload_to=get_file_path)
    why_buy_link = models.CharField(max_length=200, blank=True, default='https://www.youtube.com/embed/bM8A5BDZglk')
    appImage = models.CharField(max_length=200, blank=True)
    primary_color = models.CharField(max_length=200, blank=True)
    secondary_color = models.CharField(max_length=200, blank=True)
    accent_color = models.CharField(max_length=200, blank=True)
    bg_color = models.CharField(max_length=200, blank=True)

    admins = models.ManyToManyField(Profile, related_name='portals')

    is_paid = models.BooleanField(default=False)
    portal_price = models.DecimalField(verbose_name="Portal price", max_digits=50, decimal_places=2, default=0)

    def __str__(self):
        return self.sub_name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        HostsService.update_hosts_conf()
        create_usersteps_for_subdomain(self.sub_name)
        create_tradelines_for_subdomain(self.sub_name)

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        HostsService.update_hosts_conf()
