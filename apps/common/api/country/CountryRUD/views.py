from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser

from apps.common.models import Country
from .serializers import CountryRUDSerializer


class CountryRUDView(RetrieveUpdateDestroyAPIView):
    """View for retrieving, updating and deleting countries."""
    queryset = Country.objects.all()
    serializer_class = CountryRUDSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'slug'

    def get_queryset(self):
        return Country.objects.filter(is_active=True)
    
    def perform_destroy(self, instance):
        instance.is_active = False
        
        instance.save()
