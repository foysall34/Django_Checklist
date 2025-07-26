from rest_framework import serializers
from .models import Item
from rest_framework import serializers


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'



# class MediaItemSerializer(serializers.ModelSerializer):
#     image = serializers.ImageField(use_url=True)
#     class Meta:
#         model = MediaItem
#         fields = '__all__'





