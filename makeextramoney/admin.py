from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from django.apps import apps
from .models import *

app = apps.get_app_config('makeextramoney')
