from rest_framework.generics import CreateAPIView

from .serializers import ForwardCreateSerializer
from apps.common.models import Forward


class ForwardCreateView(CreateAPIView):
    queryset = Forward.objects.all()
    serializer_class = ForwardCreateSerializer

    def get_queryset(self):
        return self.queryset.filter(is_active=True).select_related('sender', 'receiver', 'content')

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)
