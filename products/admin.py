from django.apps import apps
from django.contrib import admin
from django.db.models.query_utils import Q

from dynamic.models import Subdomain
from .models import Tradelines, UserStepsProduct

app = apps.get_app_config('products')


class TradelinesAdmin(admin.ModelAdmin):
    list_display = (
        'company_name', 'product', 'price', 'charge', 'whitelabel_portal', 'tradeline_amount', 'company_reports_to')
    readonly_fields = ('product_id', 'price_id', 'price_lookup')
    search_fields = ('product','company_name','whitelabel_portal__sub_name',)
    actions = ('clone_tradelines_for_all_subdomains',)

    def delete_queryset(self, request, queryset):
        for product in queryset:
            product.delete()

    def clone_tradelines_for_all_subdomains(self, request, queryset):
        subdomains = Subdomain.objects.all()
        all_tradelines = Tradelines.objects.all()
        for product in queryset:
            for subdomain in subdomains:
                count = all_tradelines.filter(company_name=product.company_name,
                                              product=product.product,
                                              whitelabel_portal=subdomain,price=product.price
                                              ).count()
                if count == 0:
                    new_tradeline = product
                    new_tradeline.pk = None
                    new_tradeline.product_id = None
                    new_tradeline.whitelabel_portal = subdomain
                    new_tradeline.save()

    clone_tradelines_for_all_subdomains.short_description = "Clone tradelines for all subdomains"


admin.site.register(Tradelines, TradelinesAdmin)


class UserStepsAdmin(admin.ModelAdmin):
    list_display = ('name', 'whitelabel_portal', 'price', 'recurring',)
    readonly_fields = ('product_id', 'price_id', 'price_lookup')
    actions = ('null_whitelabel',)

    def delete_queryset(self, request, queryset):
        for product in queryset:
            product.delete()

    def null_whitelabel(self, request, queryset):
        for product in queryset:
            product.whitelabel_portal = None
            product.save()


admin.site.register(UserStepsProduct, UserStepsAdmin)
