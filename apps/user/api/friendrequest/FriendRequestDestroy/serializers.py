from rest_framework.serializers import ModelSerializer

from apps.user.models import FriendRequest


class FriendRequestDestroySerializer(ModelSerializer):
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
