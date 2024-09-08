from rest_framework.generics import UpdateAPIView

from apps.user.models import FriendRequest
from .serializers import FriendRequestUpdateSerializer\


class FriendRequestUpdateView(UpdateAPIView):
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestUpdateSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return self.queryset.filter(is_active=True).select_related('sender', 'receiver')

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)
