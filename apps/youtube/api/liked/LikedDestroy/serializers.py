from rest_framework.serializers import ModelSerializer

from apps.youtube.models import Liked


class LikedDestroySerializer(ModelSerializer):
    class Meta:
        model = Liked
        fields = ['id', 'user', 'content', 'liked', 'is_active', 'created_at', 'updated_at']
