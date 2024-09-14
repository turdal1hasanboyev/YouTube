from rest_framework.generics import ListAPIView

from apps.youtube.models import Premiera
from .serializers import PremieraListSerializer


class PremieraListView(ListAPIView):

    """
    List a premiere item.
    """

    queryset = Premiera.objects.all()
    serializer_class = PremieraListSerializer

    def get_queryset(self):
        return Premiera.objects.filter(is_active=True).select_related('content')
