from rest_framework.generics import RetrieveAPIView

from .serializers import ChannelRetrieveSerializer
from apps.common.models import Channel


class ChannelRetrieveView(RetrieveAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelRetrieveSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return Channel.objects.filter(is_active=True).select_related('author')
