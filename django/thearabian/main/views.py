from django.shortcuts import render
from django.contrib.auth.models import User, Group
from main.models import country
from rest_framework import permissions, generics
from .serializers import UserSerializer, GroupSerializer, CountrySerializer


class CountryDetailAPIView(generics.RetrieveAPIView):
    queryset = country.objects.all()
    serializer_class = CountrySerializer


country_detail_view = CountryDetailAPIView.as_view()
