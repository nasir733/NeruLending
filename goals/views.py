from django.shortcuts import render, redirect
from django.views import View


class RepairBusinessCreditView(View):
    def get(self, request):
        return render(request, "repairbusinesscredit.html")


class OfferingFinancingView(View):
    def get(self, request):
        return render(request, "offeringfinancingtocustomers.html")


class NopgBusinessView(View):
    def get(self, request):
        return render(request, 'nopgbusinesscredit.html')


class MerchantView(View):
    def get(self, request):
        return render(request, 'merchantAccount.html')


class MakeExtraMoneyView(View):
    def get(self, request):
        return render(request, 'makeextramoney.html')


class ImmediateMoneyView(View):
    def get(self, request):
        return render(request, "immediatemoney.html")


class BuildPersonalCreditView(View):
    def get(self, request):
        return render(request, "buildpersonalcredit.html")
