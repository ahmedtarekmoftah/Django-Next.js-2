from django.shortcuts import render
from django.contrib.auth.models import User, Group
from main.models import country
from rest_framework import permissions, generics, authentication
from .serializers import UserSerializer, GroupSerializer, CountrySerializer


class CountryDetailAPIView(generics.RetrieveAPIView):
    queryset = country.objects.all()
    serializer_class = CountrySerializer
    permissions_classes = [permissions.IsAdminUser]
    authentication_classes = [authentication.SessionAuthentication,
                              authentication.TokenAuthentication]


country_detail_view = CountryDetailAPIView.as_view()


class CountryListCreateDetailAPIView(generics.ListCreateAPIView):
    queryset = country.objects.all()
    serializer_class = CountrySerializer
    permissions_classes = [permissions.IsAdminUser]
    authentication_classes = [authentication.SessionAuthentication,
                              authentication.TokenAuthentication]


country_list_view = CountryListCreateDetailAPIView.as_view()
