from django.contrib import admin

from .models import Portal, PortalGoal, Profile, VirtualCard, UserData, UserSteps, NewUserCredentials

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
        "virtual_access_card_paid",
    ]
    list_filter = ("fax_number_paid", "toll_free_number_paid", "website_creation_paid", "virtual_access_card_paid",)
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


class PortalGoalAdmin(admin.ModelAdmin):
    '''
        Admin View for PortalGoal
    '''
    list_display = ("name", "profile",)
    list_filter = ('profile',)
    search_fields = ("name", "profile_user__first_name", "profile_user__last_name")
    filter_horizontal = ["portals", ]


admin.site.register(PortalGoal, PortalGoalAdmin)


class UserDataAdmin(admin.ModelAdmin):
    '''
        Admin View for PortalGoal
    '''
    # list_display = ("name",)
    # list_filter = ('profile',)
    # search_fields = ("name", "profile_user__first_name", "profile_user__last_name")
    # filter_horizontal = ["portals", ]


admin.site.register(UserData, UserDataAdmin)


class UserStepsAdmin(admin.ModelAdmin):
    '''
        Admin View for PortalGoal
    '''
    # list_display = ("name",)
    # list_filter = ('profile',)
    # search_fields = ("name", "profile_user__first_name", "profile_user__last_name")
    # filter_horizontal = ["portals", ]


admin.site.register(UserSteps, UserStepsAdmin)


class UserCredsAdmin(admin.ModelAdmin):
    '''
        Admin View for PortalGoal
    '''
    # list_display = ("name",)
    # list_filter = ('profile',)
    # search_fields = ("name", "profile_user__first_name", "profile_user__last_name")
    # filter_horizontal = ["portals", ]


admin.site.register(NewUserCredentials, UserCredsAdmin)
