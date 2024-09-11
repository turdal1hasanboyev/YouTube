from rest_framework.generics import DestroyAPIView

from .serializers import ContactDestroySerializer
from apps.common.models import Contact


class ContactDestroyView(DestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactDestroySerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return self.queryset.filter(is_active=True).select_related('author')
    
    def perform_destroy(self, instance):
        instance.is_active = False
        
        instance.save()
