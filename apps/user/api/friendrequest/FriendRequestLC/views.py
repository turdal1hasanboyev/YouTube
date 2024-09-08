from rest_framework.generics import ListCreateAPIView

from .serializers import FriendRequestLCSerializer
from apps.user.models import FriendRequest


class FriendRequestLCView(ListCreateAPIView):
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestLCSerializer

    def get_queryset(self):
        return FriendRequest.objects.filter(is_active=True).select_related('sender', 'receiver')
    
    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)
