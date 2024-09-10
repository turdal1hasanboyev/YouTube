from rest_framework.generics import RetrieveUpdateDestroyAPIView

from apps.common.models import Tag
from .serializers import TagRUDSerializer


class TagRUDView(RetrieveUpdateDestroyAPIView):
    """View for retrieving, updating and deleting tags."""
    queryset = Tag.objects.all()
    serializer_class = TagRUDSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return Tag.objects.filter(is_active=True)
    
    def perform_destroy(self, instance):
        instance.is_active = False
        
        instance.save()
