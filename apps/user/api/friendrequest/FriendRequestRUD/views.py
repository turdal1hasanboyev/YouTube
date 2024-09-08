from rest_framework.generics import RetrieveUpdateDestroyAPIView

from .serializers import FriendRequestRUDSerializer
from apps.user.models import FriendRequest


class FriendRequestRUDView(RetrieveUpdateDestroyAPIView):
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestRUDSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return FriendRequest.objects.filter(is_active=True).select_related('sender', 'receiver')
    
    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)
    
    def perform_destroy(self, instance):
        instance.is_active = False
        
        instance.save()
