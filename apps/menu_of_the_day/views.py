from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .models import MenuOfTheDay
from .serializer import MenuOfTheDaySerializer

# Create your views here.


class ListMenu(viewsets.ModelViewSet):

    b = MenuOfTheDay

    # queryset = [(MenuOfTheDay.objects.filter(days=i[0]).values('menu_name'))
    #             for i in b.DAYS_OF_WEEK]

    queryset = MenuOfTheDay.objects.all()

    serializer_class = MenuOfTheDaySerializer

    # def get_queryset(self):
    #     return self.request.MenuOfTheDay.objects.all()
