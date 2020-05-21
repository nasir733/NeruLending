from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer


class TokenObtainPairPatchedSerializer(TokenObtainPairSerializer):
    def validate(self, instance):
        r = super(TokenObtainPairPatchedSerializer, self).validate(instance)
        r.update({
            'first_name': self.user.first_name,
            'last_name': self.user.last_name,
            'email': self.user.email,
        })
        return r


class UserSerializer(serializers.BaseSerializer):
    def to_representation(self, instance):
        user = {
            'first_name': '',
            'last_name': '',
            'email': '',
        }
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user

        return {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
        }
