from dynamic.models import *
from yourplan.models import *

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


def ProfileProcessor(request):
    try:
        user = Profile.objects.get(user=request.user)

        for i, k in plans.items():
            if k.objects.filter(user=user).count() > 0:
                return {'on_payment_plan': True}
    except Exception:
        pass
    return {}


def whitelabel_processor(request):
    obj = Subdomain.objects.filter(sub_name__exact=request.host.name).first()

    # print("CONTEXT: ", obj)

    if obj:
        return {
            'dynamic': obj,
        }
    else:
        if not request.user.is_anonymous:
            portal_count = Profile.objects.get(user=request.user).portals.count()
        else:
            portal_count = 0

        return {
            'is_main_site': True,
            'iswhitelabeladmin': bool(portal_count),
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
