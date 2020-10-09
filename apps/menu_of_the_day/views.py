from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import generics

from .models import MenuOfTheDay
from .serializer import MenuOfTheDaySerializer

# Create your views here.

# class ListMenu(viewsets.ModelViewSet):

#     serializer_class = MenuOfTheDaySerializer

#     queryset = MenuOfTheDay.objects.all()

#     def list(self, request):
#         return Response(
#             self.queryset.filter(
#                 days__in=[i[0] for i in MenuOfTheDay.DAYS_OF_WEEK]).values(
#                     'menu_name').values())


class ListMenu(viewsets.ModelViewSet):

    serializer_class = MenuOfTheDaySerializer

    queryset = MenuOfTheDay.objects.all()

    # l = [i[1] for i in MenuOfTheDay.DAYS_OF_WEEK]

    # print(l)

    def list(self, request):
        return Response(
            self.queryset.filter(
                days__in=[i[0] for i in MenuOfTheDay.DAYS_OF_WEEK]).values())

    # def list(self, request):
    #     return Response(
    #         self.queryset.filter(days_in_week__in=[
    #             'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
    #             'Saturday', 'Sunday'
    #         ]).values())

    def destroy(self, request):
        pass

    def update(self, request, pk=None):
        pass
