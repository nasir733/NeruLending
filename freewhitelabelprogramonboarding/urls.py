from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import *

app_name = 'freewhitelabelprogramonboarding'
urlpatterns = [

    url('onboarding', login_required(OnboardingView.as_view(), login_url='/user/login'),
        name='onboarding'),
]
