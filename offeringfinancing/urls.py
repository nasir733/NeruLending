from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import *

app_name = 'offeringfinancing'
urlpatterns = [

    url('offeringfinancing', login_required(OfferingFinancingView.as_view(), login_url='/user/login'), name='offeringfinancing'),
]
