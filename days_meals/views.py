from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import *
from rest_framework.response import Response
from .serializers.common import *



class DaysMealsCreate(APIView):

    permission_classes = [IsAuthenticated, ]

    def post(self, request):

      request.data['owner'] = request.user.id

      day_meal__serializer = DayMealSerializer(data=request.data)

      if day_meal__serializer.is_valid():

            day_meal__serializer.save()

            return Response(data=day_meal__serializer.data, status=status.HTTP_201_CREATED)

      return Response(data=day_meal__serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class FoodComponentsCreate(APIView):

    permission_classes = [IsAdminUser, ]

    def post(self, request):

      request.data['is admin'] = request.user.id

      food_component_serializer = FoodComponentSerializer(data=request.data)

      if food_component_serializer.is_valid():

            food_component_serializer.save()

            return Response(data=food_component_serializer.data, status=status.HTTP_201_CREATED)

      return Response(data=food_component_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


