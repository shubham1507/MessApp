from django.urls import path, include

from django.contrib import admin
from rest_framework import routers
from apps.accounts.views import UserViewSet, VendorList

from apps.menu_of_the_day import views

from apps.service_and_subscription.views import ServiceSubscribe

router = routers.DefaultRouter()

router.register('MenuOfWeek', views.ListMenu, base_name='MenuOfWeek')
router.register('registration', UserViewSet)
router.register('ServiceSubscribe', ServiceSubscribe)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_auth.urls')),
    path('vendor/', VendorList.as_view()),
    path('', include(router.urls)),
    path('auth/', include('rest_auth.urls')),
]
