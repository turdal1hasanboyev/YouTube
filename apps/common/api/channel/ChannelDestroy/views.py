from rest_framework.generics import DestroyAPIView

from .serializers import ChannelDestroySerializer
from apps.common.models import Channel


class ChannelDestroyView(DestroyAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelDestroySerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return Channel.objects.filter(is_active=True).select_related('author')

    def perform_destroy(self, instance):
        instance.is_active = False

        instance.save()
