from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic.base import ContextMixin

from .models import *

class OnboardingView(View):
    def get(self, request):
        return render(request, "onboarding.html")

class WhitelabelaccessView(View):
    def get(self, request):
        return render(request, "whitelabelaccess.html")
