from rest_framework.generics import ListAPIView

from .serializers import ChannelListSerializer
from apps.common.models import Channel


class ChannelListView(ListAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelListSerializer

    def get_queryset(self):
        return self.queryset.filter(is_active=True).select_related('author')
