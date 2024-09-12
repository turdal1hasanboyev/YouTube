from rest_framework.serializers import ModelSerializer

from apps.youtube.models import Comment
from apps.user.api.user.UserLC.serializers import UserLCSerializer


class CommentUpdateSerializer(ModelSerializer):
    user = UserLCSerializer(read_only=True)
    
    class Meta:
        model = Comment
        fields = [
            'id',
            'user',
            'content',
            'comment',
            'is_active',
            'created_at',
            'updated_at',
            ]
        
        extra_kwargs = {
            'id': {'read_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }
