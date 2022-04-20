from rest_framework import serializers
from days_meals.models import DayMeal, FoodComponent



class DayMealSerializer(serializers.ModelSerializer):

    class Meta:
        model = DayMeal
        fields = ('__all__')


class FoodComponentSerializer(serializers.ModelSerializer):

    class Meta:
       model = FoodComponent
       fields = ('__all__')
