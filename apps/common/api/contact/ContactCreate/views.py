from rest_framework.generics import CreateAPIView

from .serializers import ContactCreateSerializer
from apps.common.models import Contact


class ContactCreateView(CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactCreateSerializer

    def get_queryset(self):
        return self.queryset.filter(is_active=True).select_related('author')

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
