from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.urls import reverse
from dynamic.models import subdomain


class HomePage(View):
    def get(self, request):
        request.resolver_match.app_name = 'business'
        sub_domain = request.host.name
        obj = subdomain.objects.filter(sub_name__exact=sub_domain).first()
        if obj:
            if obj.is_payment_done == True:
                if request.user.is_authenticated:
                    return render(request, 'homepage.html')
            else:
                return HttpResponseRedirect("/user/login")
        else:
            return render(request, 'homepage.html')
        


class IndexView(View):
    def get(self, request):
        sub_domain = request.host.name
        obj = subdomain.objects.filter(sub_name__exact=sub_domain).first()
        if obj:
            if obj.is_payment_done == True:
                if request.user.is_authenticated:
                    return HttpResponseRedirect(reverse("homepage"))
                return render(request, 'landingpages/index.html')
            else:
                return HttpResponseRedirect("/user/login")
        else:
            if request.user.is_authenticated:
                    return HttpResponseRedirect(reverse("homepage"))
            return render(request, 'landingpages/index.html')


class AboutUsView(View):
    def get(self, request):
        return render(request, 'landingpages/about-us.html')


class PricingView(View):
    def get(self, request):
        return render(request, 'landingpages/pricing.html')


class ServicesView(View):
    def get(self, request):
        return render(request, 'landingpages/services.html')


class FinancingView(View):
    def get(self, request):
        return render(request, 'landingpages/financing.html')


class PartnerView(View):
    def get(self, request):
        return render(request, 'landingpages/partner.html')


class ContactView(View):
    def get(self, request):
        return render(request, 'landingpages/contact.html')


class WhiteLabelView(View):
    def get(self, request):
        return render(request, 'landingpages/whitelabel.html')


class AffiliatelView(View):
    def get(self, request):
        return render(request, 'landingpages/affiliate.html')

class WebinarView(View):
    def get(self, request):
        return render(request, 'landingpages/webinar.html')


class FAQView(View):
    def get(self, request):
        return render(request, 'landingpages/faq.html')


class TestimonialsView(View):
    def get(self, request):
        return render(request, 'landingpages/testimonial.html')
