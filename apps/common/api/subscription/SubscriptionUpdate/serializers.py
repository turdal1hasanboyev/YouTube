from rest_framework.serializers import ModelSerializer

from apps.common.models import Subscription
from apps.user.api.user.UserLC.serializers import UserLCSerializer


class SubscriptionUpdateSerializer(ModelSerializer):
    user = UserLCSerializer(read_only=True)

    class Meta:
        model = Subscription
        fields = ['id', 'user', 'channel', 'created_at', 'updated_at', 'is_active']

        extra_kwargs = {
            'id': {"read_only": True},
            'created_at': {"read_only": True},
            'updated_at': {"read_only": True},
        }   
