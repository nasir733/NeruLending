from django.shortcuts import render
from django.views import View

from financing_portal.models import ProductPurchasedModel, Product


class FinancingPortalHomeView(View):

    def get(self, request):
        return render(request, 'FinancingPortalHomePage.html')


class FinancingPortalProductsPurchasedView(View):

    def get(self, request):
        prods = ProductPurchasedModel.objects.filter(user=request.user)
        return render(request, 'FinancingPortalProductsPurchased.html', {"prods": prods})


class FinancingPortalPurchaseProductsView(View):

    def get(self, request):
        prods = Product.objects.all()
        return render(request, 'FinancingPortalPurchaseProducts.html', {"prods": prods})


class FinancingPortalPaymentsView(View):

    def get(self, request):
        prods = ProductPurchasedModel.objects.filter(user=request.user)
        amount_left = 0
        payments_left = 0
        for i in prods:
            amount_left += i.amount_left
            payments_left += i.payments_left

        return render(request, 'FinancingPortalPayments.html', {
            "amount_left": amount_left,
            "payments_left": payments_left
        })
