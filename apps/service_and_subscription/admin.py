from django.contrib import admin

from .models import ServiceAndSubscription

# Register your models here.


@admin.register(ServiceAndSubscription)
class AppAdmin(admin.ModelAdmin):
    pass
