from django.shortcuts import render
from rest_framework import viewsets
from .serializer import ServiceSubscribeSerializer
from .models import ServiceAndSubscription

# Create your views here.


class ServiceSubscribe(viewsets.ModelViewSet):

    serializer_class = ServiceSubscribeSerializer
    queryset = ServiceAndSubscription.objects.all()