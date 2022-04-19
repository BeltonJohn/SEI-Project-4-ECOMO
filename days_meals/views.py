from django.shortcuts import render
from rest_framework import status

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response


class DaysMealsCreate(APIView):

    permission_classes = [IsAuthenticated, ]

    def post(self, request):

      request.data['owner'] = request.user.id

      return Response('hello world')