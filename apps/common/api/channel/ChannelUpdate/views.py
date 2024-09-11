from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly

from apps.common.models import Channel
from .serializers import ChannelUpdateSerializer


class ChannelUpdateView(UpdateAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelUpdateSerializer
    lookup_field = 'slug'
    permission_classes = [
        IsAdminUser,
        IsAuthenticated,
        IsAuthenticatedOrReadOnly,
        ]
    
    def get_queryset(self):
        return self.queryset.filter(is_active=True).select_related('author')
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    