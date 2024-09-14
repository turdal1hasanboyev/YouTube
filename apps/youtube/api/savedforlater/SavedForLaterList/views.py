from rest_framework.generics import ListAPIView

from apps.youtube.models import SavedForLater
from .serializers import SavedForLaterListSerializer


class SavedForLaterListView(ListAPIView):

    """
    List a saved for later item.
    """

    queryset = SavedForLater.objects.all()
    serializer_class = SavedForLaterListSerializer
    pagination_class = None

    def get_queryset(self):
        return SavedForLater.objects.filter(is_active=True).select_related('user', 'content')
