from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View


class HomePage(View):
    def get(self, request):
        request.resolver_match.app_name = 'business'
        return render(request, 'homepage.html')
