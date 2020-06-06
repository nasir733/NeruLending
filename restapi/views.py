from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework import viewsets
from rest_framework_simplejwt.views import TokenObtainPairView

from . import serializers as apiserializers
from business import models as businessmodels
from user import models as usermodels


class TokenObtainPairPatchedView(TokenObtainPairView):
    serializer_class = apiserializers.TokenObtainPairPatchedSerializer
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
            data = usermodels.UserData.objects.get(user=usermodels.Profile.objects.get(user=request.user))
            return Response(apiserializers.UserDataSerializer().to_representation(data))
        except usermodels.UserData.DoesNotExist:
            return Response({
                'message': 'No data in database',
            })
        except Exception as e:
            return Response({
                'message': 'error',
                'type': str(type(e)),
            })


class RegisterNewUserAPI(generics.GenericAPIView):
    serializer_class = apiserializers.NewUserSerializer

    def post(self, request, *args, **kwargs):
        try:
            userr = self.get_serializer(data=request.data)
            if userr.is_valid():
                usermodels.Profile.objects.create_user(request.data['email'],
                                                       request.data['password'],
                                                       request.data['first_name'],
                                                       request.data['last_name'],
                                                       request.data['phone_number'])
                return Response({'message': 'success'}, status=200)
            else:
                raise Exception("Form is not valid.")
        except Exception as e:
            return Response({'message': f'{e}'}, status=403)


class StarterVendorListAPI(viewsets.ModelViewSet):
    serializer_class = apiserializers.StarterVendorListSerializer
    queryset = businessmodels.StarterVendorList.objects.all()
    permission_classes = (IsAuthenticated,)


class StoreCreditVendorListAPI(viewsets.ModelViewSet):
    serializer_class = apiserializers.StoreCreditVendorListSerializer
    queryset = businessmodels.StoreCreditVendorList.objects.all()
    permission_classes = (IsAuthenticated,)


class RevolvingBusinessCreditVendorAPI(viewsets.ModelViewSet):
    serializer_class = apiserializers.RevolvingBusinessCreditVendorSerializer
    queryset = businessmodels.RevolvingBusinessCreditVendor.objects.all()
    permission_classes = (IsAuthenticated,)


class NOPGAPI(viewsets.ModelViewSet):
    serializer_class = apiserializers.NOPGSerializer
    queryset = businessmodels.Nopg.objects.all()
    permission_classes = (IsAuthenticated,)


class PersonalCreditCardAPI(viewsets.ModelViewSet):
    serializer_class = apiserializers.PersonalCreditCardSerializer
    queryset = businessmodels.PersonalCreditCard.objects.all()
    permission_classes = (IsAuthenticated,)


class BusinessCreditCardAPI(viewsets.ModelViewSet):
    serializer_class = apiserializers.BusinessCreditCardSerializer
    queryset = businessmodels.BusinessCreditCard.objects.all()
    permission_classes = (IsAuthenticated,)


class ShortTermLoanAPI(viewsets.ModelViewSet):
    serializer_class = apiserializers.ShortTermLoanSerializer
    queryset = businessmodels.ShortTermLoan.objects.all()
    permission_classes = (IsAuthenticated,)


class BusinessTermLoanAPI(viewsets.ModelViewSet):
    serializer_class = apiserializers.BusinessTermLoanSerializer
    queryset = businessmodels.BusinessTermLoan.objects.all()
    permission_classes = (IsAuthenticated,)


class SBALoanAPI(viewsets.ModelViewSet):
    serializer_class = apiserializers.SBALoanSerializer
    queryset = businessmodels.SbaLoan.objects.all()
    permission_classes = (IsAuthenticated,)


class PersonalLoanAPI(viewsets.ModelViewSet):
    serializer_class = apiserializers.PersonalLoanSerializer
    queryset = businessmodels.PersonalLoan.objects.all()
    permission_classes = (IsAuthenticated,)


class BusinessLinesOfCreditAPI(viewsets.ModelViewSet):
    serializer_class = apiserializers.BusinessLinesOfCreditSerializer
    queryset = businessmodels.LinesOfCredit.objects.all()
    permission_classes = (IsAuthenticated,)


class NoCreditCheckLoansAPI(viewsets.ModelViewSet):
    serializer_class = apiserializers.NoCreditCheckLoansSerializer
    queryset = businessmodels.NoCreditCheckLoans.objects.all()
    permission_classes = (IsAuthenticated,)


class InvoiceFactoringAPI(viewsets.ModelViewSet):
    serializer_class = apiserializers.InvoiceFactoringSerializer
    queryset = businessmodels.InvoiceFactoring.objects.all()
    permission_classes = (IsAuthenticated,)


class InvoiceFinancingAPI(viewsets.ModelViewSet):
    serializer_class = apiserializers.InvoiceFinancingSerializer
    queryset = businessmodels.InvoiceFinancing.objects.all()
    permission_classes = (IsAuthenticated,)


class EquipmentFinancingAPI(viewsets.ModelViewSet):
    serializer_class = apiserializers.EquipmentFinancingSerializer
    queryset = businessmodels.EquipmentFinancing.objects.all()
    permission_classes = (IsAuthenticated,)


class GetUserStepsAPI(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        try:
            steps = usermodels.UserSteps.objects.get(email=request.user.email)
            steps_serialized = apiserializers.UserStepsSerializer().to_representation(steps)
            return Response(steps_serialized, status=200)

        except usermodels.UserSteps.DoesNotExist:
            return Response({
                'website': 1,
                'toll_free': 1,
                'fax_number': 1,
                'domain': 1,
                'professional_email': 1,
            })

        except Exception as e:
            return Response({'message': f'{e}'}, status=403)
