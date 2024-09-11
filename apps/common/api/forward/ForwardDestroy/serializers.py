from rest_framework.serializers import ModelSerializer

from apps.common.models import Forward


class ForwardDestroySerializer(ModelSerializer):
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
