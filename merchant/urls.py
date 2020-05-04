from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import *

app_name = 'merchant'
urlpatterns = [

    url('merchant', login_required(MerchantView.as_view(), login_url='/user/login'),
        name='merchant'),
]
