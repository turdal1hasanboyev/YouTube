from rest_framework.generics import ListAPIView

from .serializers import ContactListSerializer
from apps.common.models import Contact


class ContactListView(ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactListSerializer
    pagination_class = None

    def get_queryset(self):
        return Contact.objects.filter(is_active=True).select_related('author')
