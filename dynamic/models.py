from django.db import models

from products.services import create_usersteps_for_subdomain, create_tradelines_for_subdomain
from services.FileServices import get_file_path
from services.HostsService import HostsService
from user.models import Profile

app_name = 'dynamic'

default_front_text = 'We Help Businesses Acquire Business Credit With Our Free Software, Mobile App, & Google Chrome Extension. Also, We Have A Free Personal Credit, Marketing, & Business Credit Course In Our Software As Well. Get $1,500 In Free Marketing, & Only Pay For Real Services Only When You Need It & Would Like To Upgrade & Purchase Our Business Credit Builder Package.'
default_about_text = 'Get Dinero Today offers a wide range of services. Which include getting clients loans, building business credit, $1,500 in free marketing, business credit course, autodialer, website builder and much more. Our business builder program helps you with each step of the business credit building process.'

default_credit_repair_text = """Click The Button Below To Have One On One Credit Repair 
Start Fixing Your Credit For As Low As $49.99 Per Month"""


class Subdomain(models.Model):
    # General
    is_payment_done = models.BooleanField(default=True)
    sub_name = models.CharField(max_length=300, unique=True)
    is_main_site = models.BooleanField(default=False)
    admins = models.ManyToManyField(Profile, related_name='portals')

    # Styles and Info
    can_edit = models.BooleanField(default=False)
    primary_color = models.CharField(max_length=200, blank=True)
    secondary_color = models.CharField(max_length=200, blank=True)
    accent_color = models.CharField(max_length=200, blank=True)
    bg_color = models.CharField(max_length=200, blank=True)
    login_window_color = models.CharField(max_length=200, blank=True)
    appImage = models.CharField(max_length=200, blank=True, default='/static/images/thebusinessbuildersapp.png')
    favicon = models.ImageField(upload_to=get_file_path, blank=True)
    logo = models.ImageField(upload_to=get_file_path)
    email = models.CharField(max_length=200, default='info@businesscreditbuildersllc.com', null=True, blank=True)
    title = models.CharField(max_length=200, null=True)
    favicon_title = models.CharField(verbose_name="Tab Title", max_length=200, null=True)
    seo_description = models.CharField(max_length=200, null=True)
    frontpage_text = models.TextField("Main text", default=default_front_text, null=True)
    aboutus_text = models.TextField("About Us text", default=default_about_text, null=True)
    address = models.CharField(max_length=200, null=True)
    phno = models.CharField(blank=True, max_length=100)
    show_money_back_guarantee = models.BooleanField(default=True)
    show_why_buy_from_us = models.BooleanField(default=True)
    show_appointment = models.BooleanField(default=True)

    # Links
    webinar = models.URLField(max_length=300, default='https://youtu.be/xNCfnbGT5hY')
    iphoneApp = models.URLField(max_length=300, default='https://apps.apple.com/us/app/the-business-credit-builders/id1528895728')
    androidApp = models.URLField(max_length=300, default='https://play.google.com/store/apps/details?id=com.millennialbusinessbuilders.businesscreditbuilders')
    chromeExt = models.URLField(max_length=300, default='https://chrome.google.com/webstore/detail/the-business-credit-build/jpbbaabmhfpfdjnomgdieempedlaelfi')
    homeVideo = models.URLField(max_length=300)
    extensionVideo = models.URLField(max_length=300)
    faq_page = models.CharField(max_length=300, null=True,
                                default='https://businessbuilders.zendesk.com/hc/en-us/sections/360010349512-FAQ')
    creditRepairLink = models.CharField(max_length=300, null=True, default='/business/credit-affiliate')
    appointment_link = models.CharField(max_length=200, blank=True)
    why_buy_link = models.CharField(max_length=200, blank=True, default='https://www.youtube.com/embed/bM8A5BDZglk')

    # Prices
    is_paid = models.BooleanField(default=False)
    portal_price = models.DecimalField(verbose_name="Portal price", max_digits=50, decimal_places=2, default=0)

    # White Label Section
    is_paid_for_whitelabel = models.BooleanField(default=False)
    show_index_white_label = models.BooleanField(default=False)
    show_becoming_whitelabel_partner = models.BooleanField(default=False)
    offer_paid_whitelabel = models.BooleanField(default=False)
    show_whitelabel_link = models.BooleanField(default=True)
    whitelabelpartner_link = models.CharField(max_length=200, blank=True)
    whitelabel_index_video = models.CharField(max_length=200, blank=True)
    basic_partnership_program_price = models.DecimalField(verbose_name="Basic Partnership Program Price Annual",
                                                          max_digits=50, decimal_places=2, default=2000.00)
    premium_partnership_program_price = models.DecimalField(verbose_name="Basic Partnership Program Price Monthly",
                                                            max_digits=50, decimal_places=2, default=1000.00)

    # Affiliate Section
    show_free_access_to_affiliate_program = models.BooleanField(default=False)
    show_affiliate = models.BooleanField(default=False)
    affiliate_link = models.CharField(max_length=200, blank=True)

    # Credit Repair Services
    show_credit_repair_plan = models.BooleanField(default=True)
    credit_repair_service_text = models.TextField(default=default_credit_repair_text, null=True)
    credit_repair_service_image = models.CharField(max_length=200, blank=True,
                                                   default='https://www.creditfirm.net/wp-content/uploads/2012/06/CreditFirm-Logo-300x182.jpg')
    credit_repair_service_button_text = models.CharField(max_length=200, blank=True,
                                                         default='Click Here To Get Your Free Consultation')
    credit_repair_consultation_link = models.CharField(max_length=200, blank=True,
                                                       default='https://shareasale.com/r.cfm?b=520260&u=2228198&m=49614&urllink=&afftrack=')

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
