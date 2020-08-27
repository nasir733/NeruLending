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
    obj = Subdomain.objects.filter(sub_name__exact=sub_domain).first()

    if obj:
        return {
            'wl_logo': '/static/whitelabel_data/logotrans.png',
            'phone_number': "324354656",
            'LOGIN_BG_COLOR_CSS': "white",
            'dynamic': obj,
        }
    else:
        return {
            'wl_logo': '/static/images/logo.png',
            'phone_number': "877-726-2604",
            'is_main_site': True,
            'LOGIN_BG_COLOR_CSS': "-webkit-linear-gradient(-30deg, #177b3f, #07231b)",
            'dynamic': {
                'title': 'Get Dinero Today',
                'androidApp': "https://play.google.com/store/apps/details?id=com.millennialbusinessbuilders.getdianotoday",
                'iphoneApp': "https://apps.apple.com/us/app/get-dinero-today/id1520722061",
                'chromeExt': "https://chrome.google.com/webstore/detail/get-dinero-today/nopllamladnpdgmgcfbnhdfpllpgpcgk",
                'email': " info@getdinerotoday.com",
                'phno': " 877-726-2604",
                'address': "1629 K St NW Suite 300, Washington, DC 20006",
                'sub_name': "",
            }
        }
