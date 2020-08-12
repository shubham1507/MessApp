from rest_framework import serializers

from .models import MenuOfTheDay, MealType

# class MealTypeSerializer(serializers.ModelSerializer):
#     class Meta:

#         model = MealType

#         fields = ('meal_type', )


class MenuOfTheDaySerializer(serializers.ModelSerializer):

    # meal_type = MealTypeSerializer(many=True, read_only=True)

    class Meta:

        model = MenuOfTheDay
        fields = (
            'menu_name',
            'days',
            'days_in_week',
            'meal_type',
        )
