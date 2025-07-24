# myapp/serializers.py

from rest_framework import serializers
from .models import MediaItem

class MediaItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaItem
        fields = '__all__'




class FoodImageSerializer(serializers.Serializer):
    image = serializers.ImageField()
