from rest_framework.generics import ListAPIView

from .serializers import SubscriptionListSerializer
from apps.common.models import Subscription


class SubscriptionListView(ListAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionListSerializer
    pagination_class = None

    def get_queryset(self):
        return Subscription.objects.filter(is_active=True).select_related('user', 'channel')
