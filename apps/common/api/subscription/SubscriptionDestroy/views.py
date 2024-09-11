from rest_framework.generics import DestroyAPIView

from .serializers import SubscriptionDestroySerializer
from apps.common.models import Subscription


class SubscriptionDestroyView(DestroyAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionDestroySerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return Subscription.objects.filter(is_active=True).select_related('user', 'channel')

    def perform_destroy(self, instance):
        instance.is_active = False

        instance.save()
