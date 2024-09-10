from rest_framework.generics import ListCreateAPIView

from apps.common.models import Category
from .serializers import CategoryLCSerializer


class CategoryLCView(ListCreateAPIView):
    """View for listing and creating categories."""
    queryset = Category.objects.all()
    serializer_class = CategoryLCSerializer

    def get_queryset(self):
        return self.queryset.filter(is_active=True)
