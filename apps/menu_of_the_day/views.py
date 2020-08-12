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

    l = [i[1] for i in b.DAYS_OF_WEEK]

    print(l)

    # queryset = MenuOfTheDay.objects.filter(days__in=l).values('menu_name')

    # queryset = MenuOfTheDay.objects.filter(
    #     days_in_week__in=l).values('menu_name')

    queryset = MenuOfTheDay.objects.all()

    def list(self, request):
        b = MenuOfTheDay
        return Response(
            self.queryset.filter(days__in=[i[0] for i in b.DAYS_OF_WEEK
                                           ]).values('menu_name').values())

    # def destroy(self, request, *args, **kwargs):
    #     try:
    #         instance = self.get_object()
    #         self.perform_destroy(instance)
    #     except Http404:
    #         pass
    #     return Response(status=status.HTTP_204_NO_CONTENT)

    # print(queryset)
