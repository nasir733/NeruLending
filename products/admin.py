from django.apps import apps
from django.contrib import admin

from .models import Tradelines, UserStepsProduct

app = apps.get_app_config('products')


class TradelinesAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'product', 'price', 'charge', 'whitelabel_portal', 'tradeline_amount', 'company_reports_to')
    readonly_fields = ('product_id', 'price_id', 'price_lookup')

    def delete_queryset(self, request, queryset):
        for product in queryset:
            product.delete()


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
