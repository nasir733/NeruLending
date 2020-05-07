from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import *

from django.views.generic.base import ContextMixin
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.forms import ModelForm


class HomeWhiteLabelView(View):
    def get(self, request):
        return render(request, "home-whitelabel.html")


class BecomingAPartnerForm(ModelForm):
    class Meta:
        model = BecomingAPartner
        fields = ['business_name', 'business_number', 'logo']


def BecomingAPartner_update(request, pk, template_name='becomingapartner.html'):
    lead = get_object_or_404(BecomingAPartner, pk=pk)
    form = BecomingAPartnerForm(request.POST or None, instance=lead)
    if form.is_valid():
        form.save()
        return redirect('whitelabelpartnerportal:becomingapartner')

    return render(request, template_name, {'form': form})


class BecomingAPartnerView(View):
    def get(self, request):
        partners = BecomingAPartner.objects.filter(user=Profile.objects.get(user=request.user))
        return render(request, "becomingapartner.html", {"partners": partners})

    def post(self, request):
        if 'delete' in request.POST:
            try:
                instance = BecomingAPartner.objects.get(id=request.POST['delete'])
                instance.delete()
                return redirect('whitelabelpartnerportal:becomingapartner')
            except Exception as e:
                print(e)
                return redirect('whitelabelpartnerportal:becomingapartner')

        else:
            data = {
                'business_name': request.POST['business_name'],
                'business_number': request.POST['business_number'],
            }
            if 'logo' in request.FILES:
                data['logo'] = request.FILES['logo']

            new_lead = BecomingAPartner(user=Profile.objects.get(user=request.user), **data)
            new_lead.save()
            return redirect('whitelabelpartnerportal:becomingapartner')


class WhiteLabelTrainingView(View):
    def get(self, request):
        return render(request, "whitelabeltraining.html")


class MyResidualsView(View):
    def get(self, request):
        residuals = Residual.objects.filter(user=Profile.objects.get(user=request.user))
        return render(request, "myresiduals.html", {"residuals": residuals})


class EnterNewLeadsView(View):
    def get(self, request):
        return render(request, "enternewleads.html")

    def post(self, request):
        data = {
            'first_name': request.POST['firstname'],
            'last_name': request.POST['lastname'],
            'business_name': request.POST['businessname'],
            'business_package': request.POST['businesspackage'],
        }
        new_lead = Lead(user=Profile.objects.get(user=request.user), **data)
        new_lead.save()
        return HttpResponseRedirect(reverse("whitelabelpartnerportal:leadoverview"))
        # return render(request, "enternewleads.html", {"submitted": True})


class LeadForm(ModelForm):
    class Meta:
        model = Lead
        fields = ['first_name', 'last_name', 'business_name', 'business_package']


def lead_update(request, pk, template_name='enternewleads.html'):
    lead = get_object_or_404(Lead, pk=pk)
    form = LeadForm(request.POST or None, instance=lead)
    if form.is_valid():
        form.save()
        return redirect('whitelabelpartnerportal:leadoverview')

    return render(request, template_name, {'form': form})


class LeadOverviewView(View):
    def get(self, request):
        leads = Lead.objects.filter(user=Profile.objects.get(user=request.user))
        return render(request, "leadoverview.html", {"leads": leads})

    def post(self, request):
        if 'delete' in request.POST:
            try:
                instance = Lead.objects.get(id=request.POST['delete'])
                instance.delete()
            except Exception as e:
                pass
        return HttpResponseRedirect(reverse("whitelabelpartnerportal:leadoverview"))


class MySalesView(View):
    def get(self, request):
        sales = Sale.objects.filter(user=Profile.objects.get(user=request.user))
        return render(request, "mysales.html", {"sales": sales})


class NetworkMarketingView(View):
    def get(self, request):
        return render(request, "networkmarketing.html")


class EnterAffiliatesView(View):
    def get(self, request):
        return render(request, "enteraffiliates.html")

    def post(self, request):
        data = {
            'full_name': request.POST['fullname'],
            'phone_number': request.POST['phonenumber'],

        }
        new_agent = AffiliateAgents(user=Profile.objects.get(user=request.user), **data)
        new_agent.save()
        return HttpResponseRedirect(reverse("whitelabelpartnerportal:salesaffiliates"))


class SalesAffiliatesView(View):
    def get(self, request):
        agents = AffiliateAgents.objects.filter(user=Profile.objects.get(user=request.user))

        return render(request, "salesaffiliates.html", {"agents": agents})

    def post(self, request):
        if 'delete' in request.POST:
            try:
                instance = AffiliateAgents.objects.get(id=request.POST['delete'])
                instance.delete()
            except Exception as e:
                pass
        return HttpResponseRedirect(reverse("whitelabelpartnerportal:salesaffiliates"))


class AffiliateAgentForm(ModelForm):
    class Meta:
        model = AffiliateAgents
        fields = ['full_name', 'phone_number']


def affiliate_agent_update(request, pk, template_name='enteraffiliates.html'):
    lead = get_object_or_404(AffiliateAgents, pk=pk)
    form = AffiliateAgentForm(request.POST or None, instance=lead)
    if form.is_valid():
        form.save()
        return redirect('whitelabelpartnerportal:salesaffiliates')
    return render(request, template_name, {'form': form})


class ResidualsFromAffiliatesView(View):
    def get(self, request):
        residuals = AffiliateResidual.objects.filter(user=Profile.objects.get(user=request.user))
        return render(request, "residualsfromaffiliates.html", {"residuals": residuals})


class FreeSignupView(View):
    def get(self, request):
        freeprograms = FreeProgram.objects.filter(user=Profile.objects.get(user=request.user))
        return render(request, "freesignup.html", {"freeprograms": freeprograms})


class PaidSignupView(View):
    def get(self, request):
        paidprograms = PaidProgram.objects.filter(user=Profile.objects.get(user=request.user))

        return render(request, "paidsignup.html", {"paidprograms": paidprograms})


class OrdersView(View):
    def get(self, request):
        orders = Order.objects.filter(user=Profile.objects.get(user=request.user))
        return render(request, "orders.html", {"orders": orders})


class InvoicesView(View):
    def get(self, request):
        invoices = Invoice.objects.filter(user=Profile.objects.get(user=request.user))
        return render(request, "invoices.html", {"invoices": invoices})


class PaymentsView(View):
    def get(self, request):
        payments = Payment.objects.filter(user=Profile.objects.get(user=request.user))

        return render(request, "payments.html", {"payments": payments})


class CreditsView(View):
    def get(self, request):
        credits = Credit.objects.filter(user=Profile.objects.get(user=request.user))
        return render(request, "credits.html", {"credits": credits})


class WholesalePackagesView(View):
    def get(self, request):
        return render(request, "wholesalepackages.html")


class OfferingFinancingView(View):
    def get(self, request):
        return render(request, "offeringfinancing.html")


class WhiteLabelWebinarView(View):
    def get(self, request):
        return render(request, "whitelabelwebinar.html")


class BuyWhitelabelWebsiteView(View):
    def get(self, request):
        return render(request, "buywhitelabelwebsite.html")


class BuyWhitelabelBusinessPackageView(View):
    def get(self, request):
        return render(request, "buywhitelabelbusinesspackage.html")


class ViewPortalsView(View):
    def get(self, request):
        return render(request, "viewportals.html")


class ViewWhiteLabelWebsiteView(View):
    def get(self, request):
        sites = WhitelabelWebsite.objects.filter(user=Profile.objects.get(user=request.user))

        return render(request, "viewwhitelabelwebsite.html", {"sites": sites})


class ViewWhiteLabelBusinessPackageView(View):
    def get(self, request):
        packages = WhitelabelBusinessPackage.objects.filter(user=Profile.objects.get(user=request.user))

        return render(request, "viewwhitelabelbusinesspackage.html", {"packages": packages})


class AddBankInfoView(View):
    def get(self, request):
        banks = BankPaymentInformation.objects.filter(user=Profile.objects.get(user=request.user))
        return render(request, "addbankinfo.html", {"banks": banks})

    def post(self, request):
        if 'delete' in request.POST:
            try:
                instance = BankPaymentInformation.objects.get(id=request.POST['delete'])
                instance.delete()
            except Exception as e:
                pass
        return HttpResponseRedirect(reverse("whitelabelpartnerportal:addbankinfo"))


class BankInfoForm(ModelForm):
    class Meta:
        model = BankPaymentInformation
        fields = ['routing_number', 'name_of_bank', 'account_number', 'name_on_bank_account', 'your_address']


def bank_info_update(request, pk, template_name='addbankinfo_form.html'):
    lead = get_object_or_404(BankPaymentInformation, pk=pk)
    form = BankInfoForm(request.POST or None, instance=lead)
    if form.is_valid():
        form.save()
        return redirect('whitelabelpartnerportal:addbankinfo')
    return render(request, template_name, {'form': form})


class AddBankInfoFormView(View):
    def get(self, request):
        return render(request, "addbankinfo_form.html")

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
        return HttpResponseRedirect(reverse("whitelabelpartnerportal:addbankinfo"))


class AddPaypalInfoView(View):
    def get(self, request):
        paypals = PaypalInformation.objects.filter(user=Profile.objects.get(user=request.user))
        return render(request, "addpaypalinfo.html", {"paypals": paypals})

    def post(self, request):
        if 'delete' in request.POST:
            try:
                instance = PaypalInformation.objects.get(id=request.POST['delete'])
                instance.delete()
            except Exception as e:
                pass
        return HttpResponseRedirect(reverse("whitelabelpartnerportal:addpaypalinfo"))


class AddPaypalInfoFormView(View):
    def get(self, request):
        return render(request, "addpaypalinfo_form.html")

    def post(self, request):
        data = {
            'paypal_email': request.POST['paypal_email'],
        }
        new_bank = PaypalInformation(user=Profile.objects.get(user=request.user), **data)
        new_bank.save()
        return HttpResponseRedirect(reverse("whitelabelpartnerportal:addpaypalinfo"))


class PayPalInfoForm(ModelForm):
    class Meta:
        model = PaypalInformation
        fields = ['paypal_email']


def paypal_info_update(request, pk, template_name='addpaypalinfo_form.html'):
    lead = get_object_or_404(PaypalInformation, pk=pk)
    form = PayPalInfoForm(request.POST or None, instance=lead)
    if form.is_valid():
        form.save()
        return redirect('whitelabelpartnerportal:addpaypalinfo')
    return render(request, template_name, {'form': form})


class MerchantView(View):
    def get(self, request):
        return render(request, "merchant.html")


class FaxView(View):
    def get(self, request):
        return render(request, "fax.html")


class TollFreeView(View):
    def get(self, request):
        return render(request, "tollfree.html")


class ProfessionalEmailView(View):
    def get(self, request):
        return render(request, "professionalemail.html")
