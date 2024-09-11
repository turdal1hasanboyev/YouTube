from rest_framework.generics import UpdateAPIView

from .serializers import ForwardUpdateSerializer
from apps.common.models import Forward


class ForwardUpdateView(UpdateAPIView):
    queryset = Forward.objects.all()
    serializer_class = ForwardUpdateSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return Forward.objects.filter(is_active=True).select_related('sender', 'receiver', 'content')

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)
