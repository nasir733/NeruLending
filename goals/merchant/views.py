from django.shortcuts import render
from django.views import View


class MerchantView(View):
    def get(self, request):
        return render(request, 'merchantAccount.html')
