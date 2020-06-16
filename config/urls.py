from django.urls import path, include

from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('accounts.urls')),
    path('auth/', include('rest_auth.urls'))
]