from rest_framework.generics import RetrieveAPIView

from apps.youtube.models import Liked
from .serializers import LikedRetrieveSerializer


class LikedRetrieveView(RetrieveAPIView):

    """
    Retrieve a liked object instance.
    """

    queryset = Liked.objects.all()
    serializer_class = LikedRetrieveSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return Liked.objects.filter(is_active=True).select_related('user', 'content')
    