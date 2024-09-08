from rest_framework.generics import DestroyAPIView

from apps.user.models import FriendRequest
from .serializers import FriendRequestDestroySerializer


class FriendRequestDestroyView(DestroyAPIView):
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestDestroySerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return FriendRequest.objects.filter(is_active=True).select_related('sender', 'receiver')
    
    def perform_destroy(self, instance):
        instance.is_active = False
        
        instance.save() 
