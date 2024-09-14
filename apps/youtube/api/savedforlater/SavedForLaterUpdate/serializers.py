from rest_framework.serializers import ModelSerializer

from apps.youtube.models import SavedForLater

from apps.user.api.user.UserLC.serializers import UserLCSerializer


class SavedForLaterUpdateSerializer(ModelSerializer):
    user = UserLCSerializer(read_only=True)

    class Meta:
        model = SavedForLater
        fields = [
            'id',
            'user',
            'content',
            'created_at',
            'updated_at',
            'is_active',
        ]

        extra_kwargs = {
            'id': {'read_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }
