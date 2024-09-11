from rest_framework.generics import DestroyAPIView

from .serializers import ForwardDestroySerializer
from apps.common.models import Forward


class ForwardDestroyView(DestroyAPIView):
    queryset = Forward.objects.all()
    serializer_class = ForwardDestroySerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return Forward.objects.filter(is_active=True).select_related('sender', 'receiver', 'content')
    
    def perform_destroy(self, instance):
        instance.is_active = False
        
        instance.save()
