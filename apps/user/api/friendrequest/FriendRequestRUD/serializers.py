from rest_framework.serializers import ModelSerializer

from apps.user.models import FriendRequest


class FriendRequestRUDSerializer(ModelSerializer):
    class Meta:
        model = FriendRequest
        fields = [
            'id',
            'sender',
            'receiver',
            "is_active",
            'created_at',
            'updated_at',
        ]

        extra_kwargs = {
            'id': {'read_only': True},
            'sender': {'read_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }
