from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserSerializer, CustomTokenObtainPairSerializer, ProfileSerializer
from .models import CustomUser, Profile


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        token = serializer.validated_data['access']
        refresh_token = serializer.validated_data['refresh']
        serialized_user = UserSerializer(user).data
        serialized_profile = ProfileSerializer(user.profile, many=False).data
        response_data = {
            'user': {**serialized_user, **serialized_profile},
            'token': token,
            'refresh_token': refresh_token,
        }
        return Response(response_data)
