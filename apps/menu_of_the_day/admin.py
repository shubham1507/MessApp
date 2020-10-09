from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(MenuOfTheDay)

# admin.site.register(MealType)


@admin.register(MenuOfTheDay, ServiceAndSubscription, Mealschedule)
class AppAdmin(admin.ModelAdmin):
    pass
