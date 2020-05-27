from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from user.models import UserData


class TokenObtainPairPatchedSerializer(TokenObtainPairSerializer):
    def validate(self, instance):
        r = super(TokenObtainPairPatchedSerializer, self).validate(instance)
        r.update({
            'first_name': self.user.first_name,
            'last_name': self.user.last_name,
            'email': self.user.email,
        })
        return r


class NewUserSerializer(serializers.Serializer):
    email = serializers.CharField(allow_blank=False)
    password = serializers.CharField(allow_blank=False)
    first_name = serializers.CharField(allow_blank=False)
    last_name = serializers.CharField(allow_blank=False)
    phone_number = serializers.CharField(allow_blank=False)


class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        exclude = ['user', ]
