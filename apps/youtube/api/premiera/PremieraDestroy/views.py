from rest_framework.generics import DestroyAPIView

from apps.youtube.models import Premiera
from .serializers import PremieraDestroySerializer


class PremieraDestroyView(DestroyAPIView):

    """
    Destroy a premiera item.
    """

    queryset = Premiera.objects.all()
    serializer_class = PremieraDestroySerializer
    lookup_field = 'pk'  # default is 'pk' but we're using 'id'

    def get_queryset(self):
        return self.queryset.filter(is_active=True).select_related('content')
    
    def perform_destroy(self, instance):
        instance.is_active = False

        instance.save()
