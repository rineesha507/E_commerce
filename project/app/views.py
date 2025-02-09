from django.shortcuts import render
from .serializers import ProductSerializer, CategorySerializer,RegisterSerializer,LoginSerializer,UserSerializer
from .models import Product, Category
from rest_framework import viewsets, permissions
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from rest_framework import generics
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response










class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    parser_classes = (MultiPartParser, FormParser)  # Allow file uploads
    permission_classes = [IsAuthenticated]

class RegisterView(generics.CreateAPIView):
        queryset = User.objects.all()
        serializer_class = RegisterSerializer


class LoginView(generics.CreateAPIView):
     serializer_class = LoginSerializer
     
     def post(self, request, *args, **kwargs):
          username = request.data.get('username')
          password = request.data.get('password')

          user = authenticate(username=username, password= password)

          if user is not None:
               refresh = RefreshToken.for_user(user)
               user_serializer = UserSerializer(user)
               return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'user' : user_serializer.data
               })
          else:
               return Response({'detail' : 'Invalid Credentials'}, status=401)
               





