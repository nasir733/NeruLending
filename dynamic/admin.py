from django.apps import apps
from django.contrib import admin

from products.services import create_usersteps_for_subdomain
from .models import Subdomain
# from import_export.admin import ImportExportModelAdmin
# from import_export import resources

# Register your models here.

app = apps.get_app_config('dynamic')

#
# class BookResource(resources.ModelResource):
#
#     class Meta:
#         model = Subdomain
#         fields = ('sub_name', 'phno')


class SubdomainAdmin(admin.ModelAdmin):
    list_display = ('sub_name', 'is_payment_done', 'webinar',
                    'iphoneApp', 'androidApp', 'chromeExt',
                    'homeVideo', 'email', 'title', 'address',
                    'phno', 'logo', 'why_buy_link', 'appImage',
                    'primary_color', 'secondary_color',
                    'accent_color', 'bg_color')
    filter_horizontal = ('admins',)
    actions = ['create_user_steps', 'payment_done']
    # resource_class = BookResource

    def create_user_steps(self, request, queryset):
        for subdomain in queryset:
            create_usersteps_for_subdomain(subdomain)

    def payment_done(self, request, queryset):
        for subdomain in queryset:
            subdomain.is_payment_done = True
            subdomain.save()


    create_user_steps.short_description = "Create user steps"
    payment_done.short_description = "Make Payment Done"


admin.site.register(Subdomain, SubdomainAdmin)
