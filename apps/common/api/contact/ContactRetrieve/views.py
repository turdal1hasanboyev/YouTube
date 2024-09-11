from rest_framework.generics import RetrieveAPIView

from .serializers import ContactRetrieveSerializer
from apps.common.models import Contact


class ContactRetrieveView(RetrieveAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactRetrieveSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return Contact.objects.filter(is_active=True).select_related('author')
