from rest_framework.generics import RetrieveAPIView

from apps.youtube.models import Content
from .serializers import ContentRetrieveSerializer


class ContentRetrieveView(RetrieveAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentRetrieveSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return self.queryset.filter(is_active=True).select_related('category', 'channel', 'country', 'play_list').prefetch_related('tags')
