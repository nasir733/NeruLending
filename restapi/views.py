from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from . import serializers
from user.models import UserData, Profile


class GetUserByToken(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response({
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email,
        })


class TokenObtainPairPatchedView(TokenObtainPairView):
    serializer_class = serializers.TokenObtainPairPatchedSerializer
    token_obtain_pair = TokenObtainPairView.as_view()


class UserSerializer(ModelSerializer):
    class Meta:
        model = UserData
        exclude = ['user',]


class FetchPersonalData(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            data = UserData.objects.get(user=Profile.objects.get(user=request.user))
            return Response(UserSerializer().to_representation(data))
        except UserData.DoesNotExist:
            return Response({
                'message': 'No data in database',
            })
        except Exception as e:
            return Response({
                'message': 'error',
                'type': str(type(e)),
            })