from rest_framework import serializers
from .models import Addiction, UserAddiction, UserProfile
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions


class UserProfileSerializer(serializers.ModelSerializer):
    addictions = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'addictions']



class AddictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addiction
        fields = ['id', 'name']

class SelectAddictionSerializer(serializers.Serializer):
    addictions = serializers.ListField(
        child=serializers.CharField()
    )

    def validate_addictions(self, values):
        addiction_objs = []
        for name in values:
            try:
                addiction = Addiction.objects.get(name__iexact=name)
                addiction_objs.append(addiction)
            except Addiction.DoesNotExist:
                raise serializers.ValidationError(f"{name} does not exist.")
        return addiction_objs

    def save(self, user_profile):
        user_profile.addictions.set(self.validated_data['addictions'])
        user_profile.save()
        return user_profile


