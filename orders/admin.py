from django.apps import apps
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import TradelineOrder

app = apps.get_app_config('orders')

class TradelineOrderAdmin(admin.ModelAdmin):
	list_display = ('id','user','tradeline')


admin.site.register(TradelineOrder,TradelineOrderAdmin)
