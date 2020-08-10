from django.urls import path, include

from django.contrib import admin
from rest_framework import routers

from accounts.views import VendorList
from apps.menu_of_the_day import views

router = routers.DefaultRouter()
router.register('list', views.ListMenu, base_name='list')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('accounts.urls')),
    path('auth/', include('rest_auth.urls')),
    path('vendor/', VendorList.as_view()),
    # path('listing/', views.ListMenu.as_view())
    path('', include(router.urls))
]
