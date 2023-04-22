from rest_framework import serializers 
from .models import Menu , Booking
from django.contrib.auth.models import User

class MenuSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Menu 
        fields = "__all__"


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking 
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = [ "username" , "email" , "first_name" , "password" ]