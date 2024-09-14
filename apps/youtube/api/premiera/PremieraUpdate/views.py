from rest_framework.generics import UpdateAPIView

from apps.youtube.models import Premiera
from .serializers import PremieraUpdateSerializer


class PremieraUpdateView(UpdateAPIView):

    """
    Update a premiera item.
    """

    queryset = Premiera.objects.all()
    serializer_class = PremieraUpdateSerializer
    lookup_field = 'pk'  # default is 'pk' but we're using 'id'

    def get_queryset(self):
        return self.queryset.filter(is_active=True).select_related('content')
    