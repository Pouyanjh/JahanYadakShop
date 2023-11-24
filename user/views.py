from django.shortcuts import render
from rest_framework import generics
from .models import user
from .serializers import RegisterSerializer
from django.conf import settings
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import user
from .serializers import RegisterSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username,
        token['email'] = user.email,
        token['id'] = user.id,
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



class RegisterView(generics.CreateAPIView):

    queryset = user.objects.all()
    serializer_class = RegisterSerializer