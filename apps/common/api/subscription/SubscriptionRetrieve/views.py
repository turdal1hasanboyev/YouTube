from rest_framework.generics import RetrieveAPIView

from .serializers import SubscriptionRetrieveSerializer
from apps.common.models import Subscription


class SubscriptionRetrieveView(RetrieveAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionRetrieveSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return Subscription.objects.filter(is_active=True).select_related('user', 'channel')
