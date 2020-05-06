from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import *

app_name = 'goals'

urlpatterns = [
    url('repairbusinesscredit/', login_required(RepairBusinessCreditView.as_view(), login_url='/user/login'), name='repairbusinesscredit'),
    url('repairbusinesscredit/1', login_required(RepairBusinessCreditViewOne.as_view(), login_url='/user/login'), name='repairbusinesscredit1'),
    url('repairbusinesscredit/2', login_required(RepairBusinessCreditViewTwo.as_view(), login_url='/user/login'), name='repairbusinesscredit2'),

    url('offeringfinancing/', login_required(OfferingFinancingView.as_view(), login_url='/user/login'), name='offeringfinancing'),
    url('nopgbusiness/', login_required(NopgBusinessView.as_view(), login_url='/user/login'), name='nopgbusiness'),
    url('merchant/', login_required(MerchantView.as_view(), login_url='/user/login'), name='merchant'),
    url('makeextramoney/', login_required(MakeExtraMoneyView.as_view(), login_url='/user/login'), name='makeextramoney'),

    url('immediatemoney/', login_required(ImmediateMoneyView.as_view(), login_url='/user/login'), name='immediatemoney'),
    url('immediatemoney/1', login_required(ImmediateMoneyViewOne.as_view(), login_url='/user/login'), name='immediatemoney1'),
    url('immediatemoney/2', login_required(ImmediateMoneyViewTwo.as_view(), login_url='/user/login'), name='immediatemoney2'),

    url('buildbusinesscredit/', login_required(BuildBusinessCreditView.as_view(), login_url='/user/login'), name='buildbusinesscredit'),
    url('buildbusinesscredit/1', login_required(BuildBusinessCreditViewOne.as_view(), login_url='/user/login'), name='buildbusinesscredit1'),
    url('buildbusinesscredit/2', login_required(BuildBusinessCreditViewTwo.as_view(), login_url='/user/login'), name='buildbusinesscredit2'),
    url('buildbusinesscredit/3', login_required(BuildBusinessCreditViewThree.as_view(), login_url='/user/login'), name='buildbusinesscredit3'),
    url('buildbusinesscredit/4', login_required(BuildBusinessCreditViewFour.as_view(), login_url='/user/login'), name='buildbusinesscredit4'),
    url('buildbusinesscredit/5', login_required(BuildBusinessCreditViewFive.as_view(), login_url='/user/login'), name='buildbusinesscredit5'),
    url('buildbusinesscredit/6', login_required(BuildBusinessCreditViewSix.as_view(), login_url='/user/login'), name='buildbusinesscredit6'),
    url('buildbusinesscredit/7', login_required(BuildBusinessCreditViewSeven.as_view(), login_url='/user/login'), name='buildbusinesscredit7'),

    url('buildpersonalcredit/', login_required(BuildPersonalCreditView.as_view(), login_url='/user/login'), name='buildpersonalcredit'),
    url('buildpersonalcredit/1', login_required(BuildPersonalCreditViewOne.as_view(), login_url='/user/login'), name='buildpersonalcredit1'),
    url('buildpersonalcredit/2', login_required(BuildPersonalCreditViewTwo.as_view(), login_url='/user/login'), name='buildpersonalcredit2'),
    url('buildpersonalcredit/3', login_required(BuildPersonalCreditViewThree.as_view(), login_url='/user/login'), name='buildpersonalcredit3'),

]
