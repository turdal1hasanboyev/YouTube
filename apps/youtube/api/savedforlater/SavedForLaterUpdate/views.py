from rest_framework.generics import UpdateAPIView

from apps.youtube.models import SavedForLater
from .serializers import SavedForLaterUpdateSerializer


class SavedForLaterUpdateView(UpdateAPIView):

    """
    Update a saved for later item.
    """

    queryset = SavedForLater.objects.all()
    serializer_class = SavedForLaterUpdateSerializer
    lookup_field = 'pk'  # default is 'pk' but we're using 'id'

    def get_queryset(self):
        return self.queryset.filter(is_active=True).select_related('user', 'content')
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
