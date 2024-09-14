from rest_framework.generics import CreateAPIView

from apps.youtube.models import SavedForLater
from .serializers import SavedForLaterCreateSerializer


class SavedForLaterCreateView(CreateAPIView):

    """
    Create a saved for later item.
    """

    queryset = SavedForLater.objects.all()
    serializer_class = SavedForLaterCreateSerializer

    def get_queryset(self):
        return SavedForLater.objects.filter(is_active=True).select_related('user', 'content')
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
