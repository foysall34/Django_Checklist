from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['owner'] = str(instance.owner)  # বা instance.owner.email if needed
        return rep
