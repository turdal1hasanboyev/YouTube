from rest_framework.generics import ListCreateAPIView

from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly

from apps.common.models import PlayList
from .serializers import PlayListLCSerializer


class PlayListLCView(ListCreateAPIView):
    """
    View for listing and creating playlists.
    """

    queryset = PlayList.objects.all()
    serializer_class = PlayListLCSerializer
    permission_classes = [
        IsAdminUser,
        IsAuthenticated,
        IsAuthenticatedOrReadOnly,
        ]
    pagination_class = None

    def get_queryset(self):
        return PlayList.objects.filter(is_active=True)
