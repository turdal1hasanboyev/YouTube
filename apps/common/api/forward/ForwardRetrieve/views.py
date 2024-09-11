from rest_framework.generics import RetrieveAPIView

from .serializers import ForwardRetrieveSerializer
from apps.common.models import Forward


class ForwardRetrieveView(RetrieveAPIView):
    queryset = Forward.objects.all()
    serializer_class = ForwardRetrieveSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return self.queryset.filter(is_active=True).select_related('sender', 'receiver', 'content')
