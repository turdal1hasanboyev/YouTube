from rest_framework.serializers import ModelSerializer

from apps.youtube.models import Comment


class CommentDestroySerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'content', 'comment', 'is_active', 'created_at', 'updated_at']
