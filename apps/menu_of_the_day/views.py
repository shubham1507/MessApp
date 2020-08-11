from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import generics

from .models import MenuOfTheDay
from .serializer import MenuOfTheDaySerializer

# Create your views here.


class ListMenu(viewsets.ModelViewSet):

    serializer_class = MenuOfTheDaySerializer

    b = MenuOfTheDay

    # queryset = [(MenuOfTheDay.objects.filter(days=i[0]).values('menu_name'))
    #             for i in b.DAYS_OF_WEEK]

    # queryset = MenuOfTheDay.objects.all()

    l = [i[0] for i in b.DAYS_OF_WEEK]

    print(l)

    queryset = MenuOfTheDay.objects.filter(days__in=l).values('menu_name')

    def list(self, request):
        return Response(self.queryset.values())

    # print(queryset)
