from rest_framework.serializers import ModelSerializer

from apps.youtube.models import Comment

from apps.user.api.user.UserLC.serializers import UserLCSerializer
from apps.youtube.api.content.ContentRetrieve.serializers import ContentRetrieveSerializer


class CommentRetrieveSerializer(ModelSerializer):
    user = UserLCSerializer(read_only=True)
    content = ContentRetrieveSerializer(read_only=True)
    
    class Meta:
        model = Comment
        fields = ['id', 'user', 'content', 'comment', 'is_active', 'created_at', 'updated_at']
