from rest_framework.generics import UpdateAPIView

from .serializers import ContactUpdateSerializer
from apps.common.models import Contact


class ContactUpdateView(UpdateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactUpdateSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return self.queryset.filter(is_active=True).select_related('author')

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
