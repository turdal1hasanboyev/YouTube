from rest_framework.generics import RetrieveAPIView

from apps.youtube.models import SavedForLater
from .serializers import SavedForLaterRetrieveSerializer


class SavedForLaterRetrieveView(RetrieveAPIView):

    """
    Retrieve a saved for later item.
    """

    queryset = SavedForLater.objects.all()
    serializer_class = SavedForLaterRetrieveSerializer
    lookup_field = 'pk'  # default is 'pk' but we're using 'id'

    def get_queryset(self):
        return self.queryset.filter(is_active=True).select_related('user', 'content')
