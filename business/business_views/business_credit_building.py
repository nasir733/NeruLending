from django.shortcuts import render, redirect
from django.views import View

from business.conf import get_context_for_all, industry_choices
from business.forms import BusinessCreditStepsForm
from dynamic.models import Subdomain
from products.models import Tradelines, UserStepsProduct
from user.models import Profile
from orders.models import UserSteps


class TradelinesView(View):
    def get(self, request):
        request.resolver_match.page_template = 'pages/base-business.html'
        subdomain = Subdomain.objects.filter(sub_name=request.host.name).first()
        tradelines = Tradelines.objects.filter(whitelabel_portal__sub_name=subdomain)
        return render(request, "financingProducts/tradelines.html",
                      context=get_context_for_all(request, {"tradelines": tradelines}))

    def post(self, request):
        ordering_products = []
        product_id = request.POST['product_id']
        product = Tradelines.objects.get(product_id=product_id)
        ordering_products.append({
            'name': str(product),
            'price': float(product.price) + float(product.charge),
            'quantity': 1,
            'type': 'tradeline',
            'product_id': product.product_id,
            'price_id': product.price_id,
        })
        request.session['ordering_products'] = ordering_products
        return redirect("business:stripe_checkout")


class BusinessCreditStepsView(View):

    def get_user_steps(self, request):
        subdomain = Subdomain.objects.filter(sub_name=request.host.name).first()
        user_steps = UserStepsProduct.objects.filter(whitelabel_portal=subdomain)
        user_steps_obj = {
            "website": user_steps.filter(name="Website Monthly").first(),
            "toll_free_number": user_steps.filter(name="Toll Free Number Monthly").first(),
            "fax_number": user_steps.filter(name="Fax Number Monthly").first(),
            "domain": user_steps.filter(name="Domain Monthly").first(),
            "professional_email_address": user_steps.filter(name="Professional Email Address Monthly").first(),
            "website_year": user_steps.filter(name="Website Yearly").first(),
            "toll_free_number_year": user_steps.filter(name="Toll Free Number Yearly").first(),
            "fax_number_year": user_steps.filter(name="Fax Number Yearly").first(),
            "domain_year": user_steps.filter(name="Domain Yearly").first(),
            "professional_email_address_year": user_steps.filter(name="Professional Email Address Yearly").first(),
            "business_builder_program": user_steps.filter(name="Business builder program Monthly").first(),
            "business_builder_program_year": user_steps.filter(name="Business builder program Yearly").first(),
        }
        return user_steps_obj

    def get(self, request):
        template = "businessCreditBuilding/BusinessCreditSteps.html"
        if "standalone" in request.path:
            template = "businessCreditBuilding/BusinessCreditStepsStandalone.html"
        elif "onlyprograms" in request.path:
            template = "businessCreditBuilding/BusinessCreditStepsOnlyPrograms.html"
        user_steps = self.get_user_steps(request)
        return render(request, template, context=get_context_for_all(request, {"form": BusinessCreditStepsForm(),
                                                                               "user_steps": user_steps}))

    def post(self, request):
        avail_products = self.get_user_steps(request)
        ordering_products = []
        services = {}

        for name, product in avail_products.items():
            if name in request.POST and request.POST[name] == 'on':
                ordering_products.append({
                    'name': str(product),
                    'price': float(product.price),
                    'quantity': int(request.POST.get(name + "_quantity", 1)),
                    'type': 'user_steps',
                    'product_id': product.product_id,
                    'price_id': product.price_id
                })
                service_in_model = name.replace("_year", "")
                services[service_in_model] = 2
                # if i in ['toll_free_number', 'fax_number', 'toll_free_number_year', 'fax_number_year']:
                #     services[i.replace("_year", "").replace("toll_free_number","toll_free") + "_quantity"] = request.POST.get(i + "_quantity")
                #     services[i.replace("_year", "") + "_prefix"] = request.POST.get(i + "_prefix")

        domain_name = ''
        if 'domain_name_year' in request.POST and request.POST['domain_name_year']:
            domain_name = request.POST['domain_name_year']
        if 'domain_name' in request.POST and request.POST['domain_name']:
            domain_name = request.POST['domain_name_year']
        industry_name = ''

        if 'industry_year' in request.POST and request.POST['industry_year']:
            industry_name = request.POST['industry_year']
        if 'industry' in request.POST and request.POST['industry']:
            industry_name = request.POST['industry']

        industry_choices_dict = {k: i for i, k in industry_choices}

        request.session['user_steps_data'] = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email': request.POST['email'],
            'phone': request.POST['phone'],
            'domain_name': domain_name,
            'industry_name': industry_choices_dict.get(industry_name, 1),
            **services
        }

        request.session['ordering_products'] = ordering_products
        return redirect("business:stripe_checkout")


class WebsiteCreationView(View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'buildbusinesscredit/base-buildbusinesscredit.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'

        return render(request, 'businessCreditBuilding/websiteCreation.html', context=get_context_for_all(request))


class FaxNumberView(View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'buildbusinesscredit/base-buildbusinesscredit.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        return render(request, 'businessCreditBuilding/faxNumber.html', context=get_context_for_all(request))


class TollFreeNumberOptionsView(View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'buildbusinesscredit/base-buildbusinesscredit.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'

        profile = Profile.objects.filter(user=request.user)
        toll_free_number_paid = False
        if profile:
            toll_free_number_paid = profile[0].toll_free_number_paid
        if toll_free_number_paid:
            user_steps = UserSteps.objects.filter(user=request.user)
            services = []

            for i in user_steps:
                for k in ['toll_free_number']:
                    if getattr(i, k) == 2:
                        serv = {
                            'name': k.replace('_', " "),
                            'status': 'In progress',
                            'product': 'In progress',
                            'username': getattr(i, 'toll_free_username'),
                            'password': getattr(i, 'toll_free_password')
                        }
                        services.append(serv)
                    elif getattr(i, k) == 3:
                        serv = {
                            'name': k.replace('_', " "),
                            'status': 'Done',
                            'product': getattr(i, k + '_act'),
                            'username': getattr(i, 'toll_free_username'),
                            'password': getattr(i, 'toll_free_password')
                        }
                        services.append(serv)
            context = get_context_for_all(request)
            context['services'] = services

            return render(request, 'businessCreditBuilding/tollFreeNumberPaid.html', context=context)
        return render(request, 'businessCreditBuilding/tollFreeNumber.html', context=get_context_for_all(request))

