from rest_framework.serializers import ModelSerializer

from apps.common.models import Subscription
from apps.user.api.user.UserLC.serializers import UserLCSerializer
from apps.common.api.channel.ChannelRetrieve.serializers import ChannelRetrieveSerializer


class SubscriptionRetrieveSerializer(ModelSerializer):
    user = UserLCSerializer(read_only=True)
    channel = ChannelRetrieveSerializer(read_only=True)

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
