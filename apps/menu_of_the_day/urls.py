from django.urls import path
from rest_framework_swagger.views import get_swagger_view

from . import views

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('', views.ListMenu, name='listmenu'),
]
