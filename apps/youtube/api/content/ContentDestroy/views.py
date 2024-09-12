from rest_framework.generics import DestroyAPIView

from apps.youtube.models import Content
from .serializers import ContentDestroySerializer


class ContentDestroyView(DestroyAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentDestroySerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return self.queryset.filter(is_active=True).select_related('category', 'channel', 'country', 'play_list').prefetch_related('tags')
    
    def perform_destroy(self, instance):
        instance.is_active = False

        instance.save()
