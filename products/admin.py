from django.apps import apps
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import tradelines

app = apps.get_app_config('products')

class tradelinesAdmin(admin.ModelAdmin):
	list_display = ('company_name','product','tradeline_amount','company_reports_to','cost','video_link')


admin.site.register(tradelines,tradelinesAdmin)
