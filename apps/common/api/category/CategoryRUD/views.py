from rest_framework.generics import RetrieveUpdateDestroyAPIView

from apps.common.models import Category
from .serializers import CategoryRUDSerializer


class CategoryRUDView(RetrieveUpdateDestroyAPIView):
    """View for retrieving, updating and deleting categories."""
    queryset = Category.objects.all()
    serializer_class = CategoryRUDSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return self.queryset.filter(is_active=True)
    
    def perform_destroy(self, instance):
        instance.is_active = False
        
        instance.save()
