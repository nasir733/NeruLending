from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import *

app_name = 'goals'
urlpatterns = [

    url('repairbusinesscredit', login_required(RepairBusinessCreditView.as_view(), login_url='/user/login'), name='repairbusinesscredit'),
    url('offeringfinancing', login_required(OfferingFinancingView.as_view(), login_url='/user/login'), name='offeringfinancing'),
    url('nopgbusiness', login_required(NopgBusinessView.as_view(), login_url='/user/login'), name='nopgbusiness'),
    url('merchant', login_required(MerchantView.as_view(), login_url='/user/login'), name='merchant'),
    url('makeextramoney', login_required(MakeExtraMoneyView.as_view(), login_url='/user/login'), name='makeextramoney'),
    url('immediatemoney', login_required(ImmediateMoneyView.as_view(), login_url='/user/login'), name='immediatemoney'),
    url('buildpersonalcredit', login_required(BuildPersonalCreditView.as_view(), login_url='/user/login'), name='buildpersonalcredit'),

]
