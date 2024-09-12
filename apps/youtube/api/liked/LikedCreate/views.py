from rest_framework.generics import CreateAPIView

from apps.youtube.models import Liked
from .serializers import LikedCreateSerializer


class LikedCreateView(CreateAPIView):

    """
    create a liked object instance.
    """

    queryset = Liked.objects.all()
    serializer_class = LikedCreateSerializer

    def get_queryset(self):
        return Liked.objects.filter(is_active=True).select_related('user', 'content')
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    