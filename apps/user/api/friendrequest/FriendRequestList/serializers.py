from rest_framework.serializers import ModelSerializer

from apps.user.models import FriendRequest
from apps.user.api.user.UserLC.serializers import UserLCSerializer


class FriendRequestListSerializer(ModelSerializer):
    sender = UserLCSerializer(read_only=True)
    receiver = UserLCSerializer(read_only=True)

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
