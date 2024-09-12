from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly

from apps.youtube.models import Content
from .serializers import ContentCreateSerializer


class ContentCreateView(CreateAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentCreateSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsAdminUser,
        IsAuthenticated,
        ]

    def get_queryset(self):
        return self.queryset.filter(is_active=True).select_related('category', 'channel', 'country', 'play_list').prefetch_related('tags')
