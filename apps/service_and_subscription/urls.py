from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListMenu, name='listmenu'),
]
