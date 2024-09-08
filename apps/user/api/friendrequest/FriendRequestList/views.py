from rest_framework.generics import ListAPIView

from apps.user.models import FriendRequest
from .serializers import FriendRequestListSerializer


class FriendRequestListView(ListAPIView):
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestListSerializer

    def get_queryset(self):
        return FriendRequest.objects.filter(is_active=True).select_related('sender', 'receiver')
