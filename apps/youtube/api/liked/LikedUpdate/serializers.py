from rest_framework.serializers import ModelSerializer

from apps.youtube.models import Liked
from apps.user.api.user.UserLC.serializers import UserLCSerializer


class LikedUpdateSerializer(ModelSerializer):
    user = UserLCSerializer(read_only=True)
    
    class Meta:
        model = Liked
        fields = [
            'id',
            'user',
            'content',
            'liked',
            'is_active',
            'created_at',
            'updated_at',
            ]
        
        extra_kwargs = {
            'id': {'read_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }
