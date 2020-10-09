from rest_framework import serializers

from .models import MenuOfTheDay


class MenuOfTheDaySerializer(serializers.ModelSerializer):
    class Meta:

        model = MenuOfTheDay
        fields = '__all__'
        # fields = (

        #     # 'menu_name',
        #     # 'days',
        #     # 'meal_type',
        # )
