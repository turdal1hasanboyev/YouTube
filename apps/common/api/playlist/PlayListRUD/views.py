from rest_framework.generics import RetrieveUpdateDestroyAPIView

from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly

from apps.common.models import PlayList
from .serializers import PlayListRUDSerializer


class PlayListRUDView(RetrieveUpdateDestroyAPIView):
    """
    View for retrieving, updating and deleting playlists.
    """

    queryset = PlayList.objects.all()
    serializer_class = PlayListRUDSerializer
    lookup_field = 'slug'
    permission_classes = [
        IsAdminUser,
        IsAuthenticated,
        IsAuthenticatedOrReadOnly,
        ]

    def get_queryset(self):
        return self.queryset.filter(is_active=True)
    
    def perform_destroy(self, instance):
        instance.is_active = False
        
        instance.save()
