from rest_framework.serializers import ModelSerializer

from apps.common.models import Channel
from apps.user.api.user.UserLC.serializers import UserLCSerializer


class ChannelListSerializer(ModelSerializer):
    author = UserLCSerializer(read_only=True)

    class Meta:
        model = Channel
        fields = [
            'id',
            'author',
            'name',
            'slug',
            'link',
            'description',
            'image',
            'created_at',
            'updated_at',
            'is_active',
        ]
