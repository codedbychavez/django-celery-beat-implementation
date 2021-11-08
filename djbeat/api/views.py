from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.

class create(APIView):
    def post(self, request, *args, **kwargs):
        user_message = 'Create request'
        print(user_message)
        return Response(user_message, status=status.HTTP_200_OK)
