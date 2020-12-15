from django.shortcuts import render, redirect
from django.views import View


class BusinessCredibilityChecklist(View):
    def get(self, request):
        return render(request, "BusinessCredibilityChecklist/BusinessCredibilityChecklist.html")

    def post(self, request):
        return redirect("business:stripe_checkout")