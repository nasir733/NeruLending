from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.base import ContextMixin
from .models import *
from django.urls import reverse
from django.http import HttpResponseRedirect


class MakeExtraMoneyView(View):
    def get(self, request):
        return render(request, 'makeextramoney.html')
