from rest_framework.serializers import ModelSerializer

from apps.common.models import Forward
from apps.user.api.user.UserLC.serializers import UserLCSerializer


class ForwardCreateSerializer(ModelSerializer):
    sender = UserLCSerializer(read_only=True)

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

        extra_kwargs = {
            'id': {'read_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }
