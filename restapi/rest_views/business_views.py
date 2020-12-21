from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.forms.models import model_to_dict

from business.models import CredibilitySteps, OtherChecklistSteps


class StepsChecklistAPI(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        steps = CredibilitySteps.objects.filter(user=request.user).first()
        if not steps:
            steps = CredibilitySteps(user=request.user)
            steps.save()

        othersteps = OtherChecklistSteps.objects.filter(user=request.user).first()
        if not othersteps:
            othersteps = CredibilitySteps(user=request.user)
            othersteps.save()

        steps_done = True
        for i, k in steps.__dict__.items():
            if not bool(k):
                steps_done = False

        return Response({'steps_done': steps_done, 'othersteps': model_to_dict(othersteps)})
