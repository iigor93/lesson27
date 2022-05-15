from rest_framework import generics

from authentication.models import User
from authentication.serializers import UserSerializer, UserCreateSerializer, UserUpdateSerializer


class UsersView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UsersCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UsersDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UsersUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer


class UsersDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
