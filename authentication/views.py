from django.conf import settings
from django.core.paginator import Paginator
from django.http import JsonResponse, Http404
from django.views import View
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from .models import User


import json

from rest_framework import generics
from .serializers import UserSerializer, UserCreateSerializer, UserUpdateSerializer
from rest_framework import viewsets


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
