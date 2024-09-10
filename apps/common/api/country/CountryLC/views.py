from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAdminUser

from apps.common.models import Country
from .serializers import CountryLCSerializer


class CountryLCView(ListCreateAPIView):
    """View for listing and creating countries."""
    queryset = Country.objects.all()
    serializer_class = CountryLCSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return self.queryset.filter(is_active=True)
