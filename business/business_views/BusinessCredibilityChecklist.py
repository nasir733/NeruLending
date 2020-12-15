from django.shortcuts import render, redirect
from django.views import View

from business.models import CredibilitySteps


class BusinessCredibilityChecklist(View):
    def get(self, request):
        steps = CredibilitySteps.objects.filter(user=request.user).first()
        if not steps:
            steps = CredibilitySteps(user=request.user)
            steps.save()

        page = request.session.get('page')
        request.session.pop('page') if page else None
        return render(request, "BusinessCredibilityChecklist/BusinessCredibilityChecklist.html",
                      {'page': page, 'steps': steps})

    def post(self, request):
        steps = CredibilitySteps.objects.filter(user=request.user).first()

        if not steps:
            steps = CredibilitySteps(user=request.user)
            steps.save()

        data = request.POST
        for i in data:
            if hasattr(steps, i):
                setattr(steps, i, bool(data.get(i)))
        steps.save()
        request.session['page'] = request.POST.get('page')
        return redirect('business:business_credibility_checklist')
