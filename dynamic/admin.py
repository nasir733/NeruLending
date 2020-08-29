from django.apps import apps
from django.contrib import admin
from .models import Subdomain

# Register your models here.

app = apps.get_app_config('dynamic')


class SubdomainAdmin(admin.ModelAdmin):
    list_display = ('sub_name', 'is_payment_done', 'webinar',
                    'iphoneApp', 'androidApp', 'chromeExt',
                    'homeVideo', 'email', 'title', 'address',
                    'phno', 'why_buy_link','appImage',
                    'primary_color','secondary_color',
                    'accent_color','bg_color')

admin.site.register(Subdomain, SubdomainAdmin)

