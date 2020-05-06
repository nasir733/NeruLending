from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import *

app_name = 'buildpersonalcredit'
urlpatterns = [

    url('buildpersonalcredit', login_required(RepairBusinessCreditView.as_view(), login_url='/user/login'), name='buildpersonalcredit'),
]
