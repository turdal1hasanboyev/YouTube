from rest_framework.generics import ListAPIView

from .serializers import ForwardListSerializer
from apps.common.models import Forward


class ForwardListView(ListAPIView):
    queryset = Forward.objects.all()
    serializer_class = ForwardListSerializer

    def get_queryset(self):
        return Forward.objects.filter(is_active=True).select_related('sender', 'receiver', 'content')
