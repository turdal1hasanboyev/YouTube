from rest_framework.generics import ListAPIView

from apps.youtube.models import Content
from .serializers import ContentListSerializer


class ContentListView(ListAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentListSerializer

    def get_queryset(self):
        return Content.objects.filter(is_active=True).select_related('category', 'channel', 'country', 'play_list').prefetch_related('tags')
