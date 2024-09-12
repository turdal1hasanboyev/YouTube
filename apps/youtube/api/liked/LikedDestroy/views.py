from rest_framework.generics import DestroyAPIView

from apps.youtube.models import Liked
from .serializers import LikedDestroySerializer


class LikedDestroyView(DestroyAPIView):

    """
    destroy a liked object instance.
    """

    queryset = Liked.objects.all()
    serializer_class = LikedDestroySerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return self.queryset.filter(is_active=True).select_related('user', 'content')
    
    def perform_destroy(self, instance):
        instance.is_active = False

        instance.save()
    