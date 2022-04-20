from rest_framework import serializers
from days_meals.models import DayMeal, FoodComponent
from jwt_auth.serializers import UserSerializer



class DayMealSerializer(serializers.ModelSerializer):

    owner = UserSerializer()

    class Meta:
        model = DayMeal
        fields = ('__all__')





class FoodComponentSerializer(serializers.ModelSerializer):

    class Meta:
       model = FoodComponent
       fields = ('__all__')


