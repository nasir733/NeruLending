from django.contrib import admin
from .models import Profile, VirtualCard, Portal

admin.site.site_header = "Get Dinero Today Admin"
admin.site.site_title = "Get Dinero Today"
admin.site.index_title = "Administration"
# admin.site.site_url = None


class ProfileAdmin(admin.ModelAdmin):
    '''
        Admin View for Profile
    '''
    list_display = ("user", "phone_number", "fax_number_paid", "toll_free_number_paid", "website_creation_paid",
                    "virtual_access_card_paid",)
    filds = [
        "user", "phone_number", "fax_number_paid", "toll_free_number_paid", "website_creation_paid",
        "virtual_access_card_paid", "portals",
    ]
    list_filter = ("fax_number_paid", "toll_free_number_paid", "website_creation_paid", "virtual_access_card_paid",)
    filter_horizontal = ["portals", ]
    search_fields = ('user__first_name', "user__last_name")


admin.site.register(Profile, ProfileAdmin)


class VirtualCardAdmin(admin.ModelAdmin):
    '''
        Admin View for VirtualCard
    '''
    list_display = ("user", "card_number", "mm_yy", "cvc", "zip_code", )
    list_filter = ('zip_code',)
    search_fields = ('user__username', "user__email", 'zip_code', 'card_number')


admin.site.register(VirtualCard, VirtualCardAdmin)


class PortalAdmin(admin.ModelAdmin):
    '''
        Admin View for Portal
    '''
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(Portal, PortalAdmin)
