from django.contrib import admin
from .models import Profile, VirtualCard

admin.site.register(Profile)


class VirtualCardAdmin(admin.ModelAdmin):
    '''
        Admin View for VirtualCard
    '''
    list_display = ("user", "card_number", "mm_yy", "cvc", "zip_code", )
    list_filter = ('zip_code',)
    search_fields = ('user__username', "user__email", 'zip_code', 'card_number')


admin.site.register(VirtualCard, VirtualCardAdmin)
