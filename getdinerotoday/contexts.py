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

    # print(sub_domain, obj)
    if obj:
        return {
            'dynamic': obj,
        }
    else:
        return {
            'is_main_site': True,
            'dynamic': {
                'title': 'Get Dinero Today',
                'androidApp': "https://play.google.com/store/apps/details?id=com.millennialbusinessbuilders.getdianotoday",
                'iphoneApp': "https://apps.apple.com/us/app/get-dinero-today/id1520722061",
                'chromeExt': "https://chrome.google.com/webstore/detail/get-dinero-today/nopllamladnpdgmgcfbnhdfpllpgpcgk",
                'email': " info@getdinerotoday.com",
                'phno': " 877-726-2604",
                'address': "1629 K St NW Suite 300, Washington, DC 20006",
                'why_buy_link': "https://www.youtube.com/embed/VaGu7EyHaVk",
                'appImage': "/static/images/iphonescreenshot.png",
                'sub_name': "",
                'primary_color': "#115d22",
                'secondary_color': "#dee1e6",
                'accent_color': "#1c6ef9",
                'bg_color': "-webkit-linear-gradient(-30deg, #177b3f, #07231b)",
                'logo': {"url": '/static/images/logo.png'},
            }
        }
