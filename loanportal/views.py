from django.shortcuts import render
from django.views import View
from django.views.generic.base import ContextMixin

from .models import *


class LoanApplicationView(View):

    def get(self, request):
        documents = Document.objects.filter(user=Profile.objects.get(user=request.user))
        return render(request, "loanapplication.html", {"documents": documents})

    def post(self, request):
        if request.POST.get('all_documents') == "on":
            data = {
                "document": request.FILES['Driver License / Photo Id'],
                "type": 'Driver License / Photo Id'
            }
            new_document = Document(user=Profile.objects.get(user=request.user), **data)
            new_document.save()
            data = {
                "document": request.FILES['Social Security Card'],
                "type": 'Social Security Card'
            }
            new_document = Document(user=Profile.objects.get(user=request.user), **data)
            new_document.save()
            data = {
                "document": request.FILES['Last 3 Months Of Bank Statement'],
                "type": 'Last 3 Months Of Bank Statement'
            }
            new_document = Document(user=Profile.objects.get(user=request.user), **data)
            new_document.save()

        else:
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
