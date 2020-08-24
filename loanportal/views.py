from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic.base import ContextMixin

from .models import *


class LoanApplicationView(View):


    def get(self, request):
        documents = Document.objects.filter(user=Profile.objects.get(user=request.user))
        return render(request, "loanapplication.html", {"documents": documents})

    def post(self, request):
        data = {
            "document": request.FILES['document'],
            "type": request.POST['document_type']
        }
        new_document = Document(user=Profile.objects.get(user=request.user), **data)
        new_document.save()
        return render(request, "loanapplication.html")


class LoanOffersView(ContextMixin, View):
    def get(self, request):
        loans = Loan.objects.filter(user=Profile.objects.get(user=request.user))
        return render(request, "loanoffers.html", {"loans": loans})
