from rest_framework.generics import CreateAPIView

from apps.common.models import Subscription
from .serializers import SubscriptionCreateSerializer


class SubscriptionCreateView(CreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionCreateSerializer
    
    def get_queryset(self):
        return self.queryset.filter(is_active=True).select_related('user', 'channel')
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    