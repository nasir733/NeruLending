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
    whitelabel = request.host.name

    if whitelabel == "businesscreditbuilders":
        return {
            'wl_logo': '/static/whitelabel_data/logotrans.png',
            'phone_number': "324354656",
            'LOGIN_BG_COLOR_CSS': "white",
        }

    return {
        'wl_logo': '/static/images/logo.png',
        'phone_number': "877-726-2604",
        'LOGIN_BG_COLOR_CSS': "-webkit-linear-gradient(-30deg, #177b3f, #07231b)",
        'is_main_site': True
    }
