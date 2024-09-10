from rest_framework.generics import ListCreateAPIView

from apps.common.models import Tag
from .serializers import TagLCSerializer


class TagLCView(ListCreateAPIView):
    """View for listing and creating tags."""
    queryset = Tag.objects.all()
    serializer_class = TagLCSerializer
    pagination_class = None

    def get_queryset(self):
        return Tag.objects.filter(is_active=True)
