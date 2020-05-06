from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import *

app_name = 'makeextramoney'
urlpatterns = [

    url('makeextramoney', login_required(MakeExtraMoneyView.as_view(), login_url='/user/login'),
        name='makeextramoney'),
]
