from rest_framework.generics import ListAPIView

from apps.youtube.models import Liked
from .serializers import LikedListSerializer


class LikedListView(ListAPIView):

    """
    list a liked object instance.
    """

    queryset = Liked.objects.all()
    serializer_class = LikedListSerializer

    def get_queryset(self):
        return self.queryset.filter(is_active=True).select_related('user', 'content')
    