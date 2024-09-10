from rest_framework.generics import RetrieveUpdateDestroyAPIView

from apps.common.models import SubEmail
from .serializers import SubEmailRUDSerializer


class SubEmailRUDView(RetrieveUpdateDestroyAPIView):
    """View for retrieving, updating and deleting subemails."""
    queryset = SubEmail.objects.all()
    serializer_class = SubEmailRUDSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return self.queryset.filter(is_active=True)
    
    def perform_destroy(self, instance):
        instance.is_active = False
        
        instance.save()
