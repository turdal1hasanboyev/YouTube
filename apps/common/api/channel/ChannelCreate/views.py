from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly

from apps.common.models import Channel
from .serializers import ChannelCreateSerializer


class ChannelCreateView(CreateAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelCreateSerializer
    permission_classes = [
        IsAdminUser,
        IsAuthenticated,
        IsAuthenticatedOrReadOnly,
        ]
    
    def get_queryset(self):
        return self.queryset.filter(is_active=True).select_related('author')
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    