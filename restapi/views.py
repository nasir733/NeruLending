from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import TokenObtainPairPatchedSerializer, NewUserSerializer, UserDataSerializer
from user.models import UserData, Profile


class TokenObtainPairPatchedView(TokenObtainPairView):
    serializer_class = TokenObtainPairPatchedSerializer
    token_obtain_pair = TokenObtainPairView.as_view()


class GetUserByToken(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response({
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email,
        })


class FetchPersonalData(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            data = UserData.objects.get(user=Profile.objects.get(user=request.user))
            return Response(UserDataSerializer().to_representation(data))
        except UserData.DoesNotExist:
            return Response({
                'message': 'No data in database',
            })
        except Exception as e:
            return Response({
                'message': 'error',
                'type': str(type(e)),
            })


class RegisterNewUserAPI(generics.GenericAPIView):
    serializer_class = NewUserSerializer

    def post(self, request, *args, **kwargs):
        try:
            userr = self.get_serializer(data=request.data)
            if userr.is_valid():
                Profile.objects.create_user(request.data['email'],
                                            request.data['password'],
                                            request.data['first_name'],
                                            request.data['last_name'],
                                            request.data['phone_number'])
                return Response({'message': 'success'}, status=200)
            else:
                raise Exception("Form is not valid.")
        except Exception as e:
            return Response({'message': f'{e}'}, status=403)
