from rest_framework.generics import CreateAPIView

from apps.youtube.models import Premiera
from .serializers import PremieraCreateSerializer


class PremieraCreateView(CreateAPIView):

    """
    Create a premiere item.
    """

    queryset = Premiera.objects.all()
    serializer_class = PremieraCreateSerializer

    def get_queryset(self):
        return Premiera.objects.filter(is_active=True).select_related('content')
    