from rest_framework.generics import DestroyAPIView

from apps.youtube.models import SavedForLater
from .serializers import SavedForLaterDestroySerializer


class SavedForLaterDestroyView(DestroyAPIView):

    """
    Destroy a saved for later item.
    """

    queryset = SavedForLater.objects.all()
    serializer_class = SavedForLaterDestroySerializer
    lookup_field = 'pk'  # default is 'pk' but we're using 'id'

    def get_queryset(self):
        return self.queryset.filter(is_active=True).select_related('user', 'content')
    
    def perform_destroy(self, instance):
        instance.is_active = False

        instance.save()
