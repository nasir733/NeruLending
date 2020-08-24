from django.apps import apps
from django.contrib import admin

# Register your models here.
from .models import *

app = apps.get_app_config('dynamic')


for model in app.get_models():
    admin.site.register(model)

