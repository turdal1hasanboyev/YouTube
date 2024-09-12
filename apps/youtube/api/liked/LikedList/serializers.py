from rest_framework.serializers import ModelSerializer

from apps.youtube.models import Liked

from apps.user.api.user.UserLC.serializers import UserLCSerializer
from apps.youtube.api.content.ContentRetrieve.serializers import ContentRetrieveSerializer


class LikedListSerializer(ModelSerializer):
    user = UserLCSerializer(read_only=True)
    content = ContentRetrieveSerializer(read_only=True)
    
    class Meta:
        model = Liked
        fields = ['id', 'user', 'content', 'liked', 'is_active', 'created_at', 'updated_at']
