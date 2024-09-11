from rest_framework.serializers import ModelSerializer

from apps.common.models import Channel


class ChannelDestroySerializer(ModelSerializer):
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
