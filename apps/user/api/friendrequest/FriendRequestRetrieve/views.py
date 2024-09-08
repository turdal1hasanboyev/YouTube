from rest_framework.generics import RetrieveAPIView

from apps.user.models import FriendRequest
from .serializers import FriendRequestRetrieveSerializer


class FriendRequestRetrieveView(RetrieveAPIView):
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestRetrieveSerializer
    lookup_field = "pk"

    def get_queryset(self):
        return self.queryset.filter(is_active=True).select_related('sender', 'receiver')
