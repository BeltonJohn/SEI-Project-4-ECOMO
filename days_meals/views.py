from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response



class DaysMealsCreate(APIView):

    permission_classes = [IsAuthenticated, ]

    def post(self, request):

      request.data['owner'] = request.user.id

      return Response('hello world')






class FoodComponentsCreate(APIView):

    permission_classes = [IsAdminUser, ]

    def post(self, request):

      request.data['is admin'] = request.user.id

      return Response('carbon crazy')

