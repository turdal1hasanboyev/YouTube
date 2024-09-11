from rest_framework.generics import UpdateAPIView

from apps.common.models import Subscription
from .serializers import SubscriptionUpdateSerializer


class SubscriptionUpdateView(UpdateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionUpdateSerializer
    lookup_field = 'pk'
    
    def get_queryset(self):
        return self.queryset.filter(is_active=True).select_related('user', 'channel')
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    