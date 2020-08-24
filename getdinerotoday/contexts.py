from dynamic.models import *
from yourplan.models import *


def ProfileProcessor(request):
    try:
        user = Profile.objects.get(user=request.user)
        plans = {
            "sezzle": Sezzle,
            "klarna": Klarna,
            "viabill": Viabill,
            "regularpayment": RegularPayment,
            "paypal": Paypal,
            "quadpay": Quadpay,
            "affirm": Affirm,
            "behalf": Behalf,
            "fundboxpay": FundBoxPay,
            "invoicefactoringpayment": InvoiceFactoringPayment,
            "stripe": Stripe,

        }
        for i, k in plans.items():
            filter = k.objects.filter(user=user)
            if len(filter) > 0:
                return {'on_payment_plan': True}
    except Exception as e:
        pass
    return {}


def whitelabel_processor(request):
    sub_domain = request.host.name
    obj = subdomain.objects.filter(sub_name=sub_domain).first()

    if obj:
        if sub_domain == 'businesscreditbuilders':
            return {
                'wl_logo': '/static/whitelabel_data/logotrans.png',
                'phone_number': "324354656",
                'LOGIN_BG_COLOR_CSS': "white",
                'dynamic': obj,
            }

    return {
        'wl_logo': '/static/images/logo.png',
        'phone_number': "877-726-2604",
        'is_main_site': True,
        'LOGIN_BG_COLOR_CSS': "-webkit-linear-gradient(-30deg, #177b3f, #07231b)",
        'dynamic': subdomain.objects.get(sub_name='localhost'),
    }
