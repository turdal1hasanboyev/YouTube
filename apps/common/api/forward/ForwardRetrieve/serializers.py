from rest_framework.serializers import ModelSerializer

from apps.common.models import Forward
from apps.user.api.user.UserLC.serializers import UserLCSerializer
from apps.youtube.api.content.ContentRetrieve.serializers import ContentRetrieveSerializer


class ForwardRetrieveSerializer(ModelSerializer):
    sender = UserLCSerializer(read_only=True)
    receiver = UserLCSerializer(read_only=True)
    content = ContentRetrieveSerializer(read_only=True)

    class Meta:
        model = Forward
        fields = [
            'id',
            'sender',
            'receiver',
            'message',
            'link',
            'content',
            'is_active',
            'created_at',
            'updated_at',
        ]
