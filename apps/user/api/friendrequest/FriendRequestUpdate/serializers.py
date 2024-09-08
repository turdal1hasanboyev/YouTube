from rest_framework.serializers import ModelSerializer

from apps.user.models import FriendRequest
from apps.user.api.user.UserLC.serializers import UserLCSerializer


class FriendRequestUpdateSerializer(ModelSerializer):
    sender = UserLCSerializer(read_only=True)

    class Meta:
        model = FriendRequest
        fields = [
            'id',
            'sender',
            'receiver',
            'is_active',
            'updated_at',
            "created_at",
        ]

        extra_kwargs = {
            'id': {'read_only': True},
            'updated_at': {'read_only': True},
            'created_at': {'read_only': True},
        }
