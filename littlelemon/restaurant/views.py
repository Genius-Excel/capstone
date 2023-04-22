from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .serializers import MenuSerialzer , BookingSerializer , UserSerializer , User
from .models import Menu , Booking
from rest_framework import viewsets 
from rest_framework import permissions
# Create your views here.

class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerialzer 

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class  = MenuSerialzer 
    permission_classes = [permissions.IsAuthenticated]

class BookingViewset(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserDetailView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer 
    permission_classes = [permissions.IsAuthenticated]

class CreateUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer 
    permission_classes = [permissions.IsAuthenticated]