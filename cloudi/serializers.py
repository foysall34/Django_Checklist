# myapp/serializers.py

from rest_framework import serializers
from .models import MediaItem

class MediaItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaItem
        fields = '__all__'


# for logMeal api intregation 

class FoodImageSerializer(serializers.Serializer):
    image = serializers.ImageField()


# serializers.py
from rest_framework import serializers
from .models import APIUser

class APIUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = APIUser
        fields = '__all__'
