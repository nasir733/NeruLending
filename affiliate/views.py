from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import *

from django.views.generic.base import ContextMixin
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.forms import ModelForm


class HomeAffiliateView(View):
    def get(self, request):
        return render(request, "home-affiliate.html")

class ShareLinksView(View):
    def get(self, request):
        return render(request, "affiliate-sharelinks.html")

class MyResidualsView(View):
    def get(self, request):
        residuals = Residual.objects.filter(user=Profile.objects.get(user=request.user))
        return render(request, "affiliate-myresiduals.html", {"residuals": residuals})


class EnterNewLeadsView(View):
    def get(self, request):
        return render(request, "affiliate-enternewleads.html")

    def post(self, request):

        data = {
            'first_name': request.POST['firstname'],
            'last_name': request.POST['lastname'],
            'business_name': request.POST['businessname'],
            'business_package': request.POST['businesspackage'],
        }
        new_lead = Lead(user=Profile.objects.get(user=request.user), **data)
        new_lead.save()
        return HttpResponseRedirect(reverse("affiliate:affiliate-leadoverview"))
        # return render(request, "enternewleads.html", {"submitted": True})


class LeadForm(ModelForm):
    class Meta:
        model = Lead
        fields = ['first_name', 'last_name', 'business_name', 'business_package']


def lead_update(request, pk, template_name='affiliate-enternewleads.html'):
    lead = get_object_or_404(Lead, pk=pk)
    form = LeadForm(request.POST or None, instance=lead)
    if form.is_valid():
        form.save()
        return redirect('affiliate:affiliate-leadoverview')

    return render(request, template_name, {'form': form})


class LeadOverviewView(View):
    def get(self, request):
        leads = Lead.objects.filter(user=Profile.objects.get(user=request.user))
        return render(request, "affiliate-leadoverview.html", {"leads": leads})

    def post(self, request):
        if 'delete' in request.POST:
            try:
                instance = Lead.objects.get(id=request.POST['delete'])
                instance.delete()
            except Exception as e:
                pass
        return HttpResponseRedirect(reverse("affiliate:affiliate-leadoverview"))


class MySalesView(View):
    def get(self, request):
        sales = Sale.objects.filter(user=Profile.objects.get(user=request.user))
        return render(request, "affiliate-mysales.html", {"sales": sales})


class NetworkMarketingView(View):
    def get(self, request):
        return render(request, "affiliate-networkmarketing.html")


class AddBankInfoView(View):
    def get(self, request):
        banks = BankPaymentInformation.objects.filter(user=Profile.objects.get(user=request.user))
        return render(request, "affiliate-addbankinfo.html", {"banks": banks})

    def post(self, request):
        if 'delete' in request.POST:
            try:
                instance = BankPaymentInformation.objects.get(id=request.POST['delete'])
                instance.delete()
            except Exception as e:
                pass
        return HttpResponseRedirect(reverse("affiliate:affiliate-addbankinfo"))


class BankInfoForm(ModelForm):
    class Meta:
        model = BankPaymentInformation
        fields = ['routing_number', 'name_of_bank', 'account_number', 'name_on_bank_account', 'your_address']


def bank_info_update(request, pk, template_name='affiliate-addbankinfo_form.html'):
    lead = get_object_or_404(BankPaymentInformation, pk=pk)
    form = BankInfoForm(request.POST or None, instance=lead)
    if form.is_valid():
        form.save()
        return redirect('affiliate:affiliate-addbankinfo')
    return render(request, template_name, {'form': form})


class AddBankInfoFormView(View):
    def get(self, request):
        return render(request, "affiliate-addbankinfo_form.html")

    def post(self, request):
        data = {
            'routing_number': request.POST['routing_number'],
            'name_of_bank': request.POST['name_of_bank'],
            'account_number': request.POST['account_number'],
            'name_on_bank_account': request.POST['name_on_bank_account'],
            'your_address': request.POST['your_address'],

        }
        new_bank = BankPaymentInformation(user=Profile.objects.get(user=request.user), **data)
        new_bank.save()
        return HttpResponseRedirect(reverse("affiliate:affiliate-addbankinfo"))





class AddPaypalInfoView(View):
    def get(self, request):
        paypals = PaypalInformation.objects.filter(user=Profile.objects.get(user=request.user))
        return render(request, "affiliate-addpaypalinfo.html", {"paypals": paypals})

    def post(self, request):
        if 'delete' in request.POST:
            try:
                instance = PaypalInformation.objects.get(id=request.POST['delete'])
                instance.delete()
            except Exception as e:
                pass
        return HttpResponseRedirect(reverse("affiliate:affiliate-addpaypalinfo"))


class AddPaypalInfoFormView(View):
    def get(self, request):
        return render(request, "affiliate-addpaypalinfo_form.html")

    def post(self, request):
        data = {
            'paypal_email': request.POST['paypal_email'],
        }
        new_bank = PaypalInformation(user=Profile.objects.get(user=request.user), **data)
        new_bank.save()
        return HttpResponseRedirect(reverse("affiliate:affiliate-addpaypalinfo"))


class PayPalInfoForm(ModelForm):
    class Meta:
        model = PaypalInformation
        fields = ['paypal_email']


def paypal_info_update(request, pk, template_name='affiliate-addpaypalinfo_form.html'):
    lead = get_object_or_404(PaypalInformation, pk=pk)
    form = PayPalInfoForm(request.POST or None, instance=lead)
    if form.is_valid():
        form.save()
        return redirect('affiliate:affiliate-addpaypalinfo')
    return render(request, template_name, {'form': form})