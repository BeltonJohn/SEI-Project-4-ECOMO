from rest_framework import serializers
from days_meals.models import DayMeal, FoodComponent
from jwt_auth.serializers import UserSerializer


class FoodComponentSerializer(serializers.ModelSerializer):

    class Meta:
       model = FoodComponent
       fields = ('__all__')


class DayMealSerializer(serializers.ModelSerializer):

    owner = UserSerializer()
    items = FoodComponentSerializer(many=True)

    class Meta:
        model = DayMeal
        fields = ('__all__')


class CreateDayMealSerializer(serializers.ModelSerializer):

    class Meta:
        model = DayMeal
        fields = ('__all__')



