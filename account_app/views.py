from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from . serializer import AccountSerializer
from rest_framework.authtoken.models import Token


class UserRegister(APIView):
    def post(self, request):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username'].lower()
            password = serializer.validated_data['password']
            user = User.objects.create_user(username=username, password=password)
            token = Token.objects.create(user=user)
            user.save()
            return Response({"message": f"User created successfully\n Token = {token}"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

