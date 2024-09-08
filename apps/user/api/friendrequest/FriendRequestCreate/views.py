from rest_framework.generics import CreateAPIView

from apps.user.models import FriendRequest
from .serializers import FriendRequestCreateSerializer


class FriendRequestCreateView(CreateAPIView):
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestCreateSerializer

    def get_queryset(self):
        return FriendRequest.objects.filter(is_active=True).select_related('sender', 'receiver')
    
    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)
