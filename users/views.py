<<<<<<< HEAD
from django.contrib.auth.models import User
from rest_framework import generics, permissions, status
from rest_framework.response import Response

class RegisterView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if not username or not password:
            return Response({"error": "username and password required"}, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(username=username).exists():
            return Response({"error": "username already exists"}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.create_user(username=username, password=password)
        return Response({"message": "user created", "id": user.id}, status=status.HTTP_201_CREATED)
=======
from django.shortcuts import render

# Create your views here.
>>>>>>> main
