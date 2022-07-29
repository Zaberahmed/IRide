
from django.shortcuts import render
from Iride_app import models
from .serializer import Rider_serializer
from rest_framework import generics


class List_rider(generics.ListCreateAPIView):
    queryset = models.Rider.objects.all()
    serializer_class = Rider_serializer


class Detail_rider(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Rider.objects.all()
    serializer_class = Rider_serializer
