from rest_framework.serializers import ModelSerializer

from apps.common.models import Subscription


class SubscriptionDestroySerializer(ModelSerializer):
    class Meta:
        model = Subscription
        fields = [
            'id',
            'user',
            'channel',
            'created_at',
            'updated_at',
            'is_active',
        ]
