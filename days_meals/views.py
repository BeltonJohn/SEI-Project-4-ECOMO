from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import *
from rest_framework.response import Response
from .serializers.common import *
from .models import DayMeal



class DaysMealsList(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request):

      meals = DayMeal.objects.filter(owner = request.user.id)

      serialized_meals = DayMealSerializer(meals, many=True)

      return Response(serialized_meals.data)
 

class DaysMealsCreate(APIView):

    permission_classes = [IsAuthenticated, ]

    def post(self, request):

      request.data['owner'] = request.user.id
      print(request.user.id)
      day_meal__serializer = DayMealSerializer(data=request.data)

      if day_meal__serializer.is_valid():

            day_meal__serializer.save()

            return Response(data=day_meal__serializer.data, status=status.HTTP_201_CREATED)

      return Response(data=day_meal__serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class FoodComponentsList(ListAPIView):

    queryset = FoodComponent.objects.all()

    serializer_class = FoodComponentSerializer




class FoodComponentsCreate(APIView):

    permission_classes = [IsAdminUser, ]

    def post(self, request):

      request.data['is admin'] = request.user.id

      food_component_serializer = FoodComponentSerializer(data=request.data)

      if food_component_serializer.is_valid():

            food_component_serializer.save()

            return Response(data=food_component_serializer.data, status=status.HTTP_201_CREATED)

      return Response(data=food_component_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class FoodComponentsUpdateDestroy(RetrieveUpdateDestroyAPIView):

    permission_classes = [IsAdminUser, ]

    queryset = FoodComponent.objects.all()

    serializer_class = FoodComponentSerializer










