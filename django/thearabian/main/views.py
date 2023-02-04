from django.shortcuts import render
from django.contrib.auth.models import User, Group
from main.models import country
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer, GroupSerializer, CountrySerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [AllowAny]


class CountryViewSet(viewsets.ModelViewSet):
    queryset = country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [AllowAny]
