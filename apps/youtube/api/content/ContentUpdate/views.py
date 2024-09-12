from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly

from apps.youtube.models import Content
from .serializers import ContentUpdateSerializer


class ContentUpdateView(UpdateAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentUpdateSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsAdminUser,
        IsAuthenticated,
        ]
    lookup_field = 'slug'

    def get_queryset(self):
        return Content.objects.filter(is_active=True).select_related('category', 'channel', 'country', 'play_list').prefetch_related('tags')
