from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.shortcuts import render


class HomePage(View):
    def get(self, request):
        request.resolver_match.app_name = 'business'
        return render(request, 'homepage.html')
