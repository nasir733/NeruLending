from django.shortcuts import render
from django.views import View


class RepairBusinessCreditView(View):
    def get(self, request):
        return render(request, "buildpersonalcredit.html")
