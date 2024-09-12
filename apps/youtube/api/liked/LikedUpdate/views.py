from rest_framework.generics import UpdateAPIView

from apps.youtube.models import Liked
from .serializers import LikedUpdateSerializer


class LikedUpdateView(UpdateAPIView):

    """
    update a liked object instance.
    """

    queryset = Liked.objects.all()
    serializer_class = LikedUpdateSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return self.queryset.filter(is_active=True).select_related('user', 'content')
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    