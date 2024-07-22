from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Car, Country, Part
from .serializers import CarSerializer, CountrySerializer, PartSerializer

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class CarAPIList(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarAPIUpdate(generics.UpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CountryAPIList(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CountryAPIUpdate(generics.UpdateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CountryAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class PartAPIList(generics.ListCreateAPIView):
    queryset = Part.objects.all()
    serializer_class = PartSerializer


class PartAPIUpdate(generics.UpdateAPIView):
    queryset = Part.objects.all()
    serializer_class = PartSerializer


class PartAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Part.objects.all()
    serializer_class = PartSerializer
