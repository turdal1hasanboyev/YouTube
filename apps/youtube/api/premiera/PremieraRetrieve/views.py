from rest_framework.generics import RetrieveAPIView

from apps.youtube.models import Premiera
from .serializers import PremieraRetrieveSerializer


class PremieraRetrieveView(RetrieveAPIView):

    """
    Retrieve a premiere item.
    """

    queryset = Premiera.objects.all()
    serializer_class = PremieraRetrieveSerializer
    lookup_field = 'pk'  # default is 'pk' but we're using 'id'

    def get_queryset(self):
        return self.queryset.filter(is_active=True).select_related('content')
